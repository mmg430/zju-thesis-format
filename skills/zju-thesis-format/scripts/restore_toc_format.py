#!/usr/bin/env python3
"""Restore source-derived formatting after WPS generates a complete TOC.

Writes a new copy only. Does not update fields, edit headings or verify rendering.
The bundled profile is for the explicitly selected built-in format only.
"""
import argparse
from copy import deepcopy
from io import BytesIO
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile, BadZipFile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
ET.register_namespace('w', W[1:-1])


class TocError(ValueError):
    pass


def parse_profile(path):
    profile = json.loads(Path(path).read_text(encoding='utf-8'))
    if profile.get('schema') != 1 or not profile.get('levels'):
        raise TocError('Unsupported formatting profile.')
    result = {}
    for level, values in profile['levels'].items():
        items = {key: ET.fromstring(values[key]) for key in ('paragraph', 'label', 'page')}
        if items['paragraph'].tag != W + 'pPr' or any(
            items[key].tag != W + 'rPr' for key in ('label', 'page')
        ):
            raise TocError('Profile must contain paragraph and run properties only.')
        if items['paragraph'].find(W + 'pStyle') is not None:
            raise TocError('Profile must not contain source style IDs.')
        # Do not permit text, field instructions or references in a format profile.
        allowed_roots = {W + 'pPr', W + 'rPr'}
        for node in items.values():
            if any(n.tag in {W + 't', W + 'instrText', W + 'fldChar', W + 'hyperlink'}
                   or n.tag == W + 'pStyle' for n in node.iter()):
                raise TocError('Profile contains non-formatting content.')
            if node.tag not in allowed_roots:
                raise TocError('Invalid profile root.')
        result[int(level)] = items
    return result


def page_range(runs):
    stack, ranges = [], []
    for index, run in enumerate(runs):
        for node in run:
            if node.tag == W + 'fldChar':
                kind = node.get(W + 'fldCharType')
                if kind == 'begin':
                    stack.append({'start': index, 'code': ''})
                elif kind == 'end' and stack:
                    field = stack.pop()
                    if field['code'].strip().startswith('PAGEREF '):
                        ranges.append((field['start'], index))
            elif node.tag == W + 'instrText' and stack:
                stack[-1]['code'] += node.text or ''
    if any(not f['code'].strip().startswith('TOC ') for f in stack) or len(ranges) != 1:
        raise TocError('Unsupported or unbalanced TOC entry fields.')
    return ranges[0]


def toc_result_runs(doc):
    stack, result = [], set()
    for run in doc.iter(W + 'r'):
        for node in run:
            active = any(f['result'] and re.match(r'^\s*TOC\s', f['code']) for f in stack)
            if active:
                result.add(run)
            if node.tag == W + 'fldChar':
                kind = node.get(W + 'fldCharType')
                if kind == 'begin':
                    stack.append({'code': '', 'result': False})
                elif kind == 'separate' and stack:
                    stack[-1]['result'] = True
                elif kind == 'end':
                    if not stack:
                        raise TocError('Unbalanced document fields.')
                    stack.pop()
            elif node.tag == W + 'instrText' and stack:
                stack[-1]['code'] += node.text or ''
    if stack:
        raise TocError('Unbalanced document fields.')
    return result


def restore(input_path, output_path, profile_path):
    source, output = Path(input_path), Path(output_path)
    if source.resolve() == output.resolve() or output.exists():
        raise TocError('Use a new output file; existing files are never overwritten.')
    profile = parse_profile(profile_path)
    with ZipFile(source) as zin:
        infos = zin.infolist()
        if len({i.filename for i in infos}) != len(infos):
            raise TocError('Duplicate package parts are unsupported.')
        parts = {info.filename: zin.read(info.filename) for info in infos}
    namespaces = {}
    for _, (prefix, uri) in ET.iterparse(BytesIO(parts['word/document.xml']), events=['start-ns']):
        if prefix in namespaces and namespaces[prefix] != uri:
            raise TocError('Nested namespace prefix rebinding is unsupported.')
        namespaces[prefix] = uri
        if re.fullmatch(r'ns[0-9]+', prefix):
            raise TocError('Unsupported namespace prefix; save the input in WPS before restoration.')
        ET.register_namespace(prefix, uri)
    doc = ET.fromstring(parts['word/document.xml'])
    styles = ET.fromstring(parts['word/styles.xml'])
    names = {s.get(W + 'styleId'): s.find(W + 'name').get(W + 'val', '')
             for s in styles.findall(W + 'style') if s.find(W + 'name') is not None}
    instructions_before = [i.text for i in doc.iter(W + 'instrText')]
    if sum(bool(re.match(r'^\s*TOC\s', i or '')) for i in instructions_before) != 1:
        raise TocError('This helper supports one complex TOC field only.')
    bookmarks_before = [(n.tag, dict(n.attrib)) for n in doc.iter()
                        if n.tag in {W + 'bookmarkStart', W + 'bookmarkEnd'}]
    eligible = toc_result_runs(doc)
    count = 0
    for paragraph in doc.iter(W + 'p'):
        old = paragraph.find(W + 'pPr')
        ps = old.find(W + 'pStyle') if old is not None else None
        name = names.get(ps.get(W + 'val') if ps is not None else '', '')
        level = re.fullmatch(r'(?:toc|目录)\s*([1-9])', name, re.IGNORECASE)
        if not level:
            continue
        codes = [i.text or '' for i in paragraph.iter(W + 'instrText')]
        if not any(re.match(r'^\s*PAGEREF\s', i) for i in codes):
            continue
        level = int(level.group(1))
        if level not in profile:
            raise TocError('TOC level is missing from the selected profile.')
        runs = list(paragraph.iter(W + 'r'))
        if not any(run in eligible for run in runs):
            continue
        start, end = page_range(runs)
        pp = deepcopy(profile[level]['paragraph'])
        pp.insert(0, deepcopy(ps))
        paragraph.remove(old)
        paragraph.insert(0, pp)
        for index, run in enumerate(runs):
            is_page = start <= index <= end
            if not is_page and run.find(W + 't') is None and run.find(W + 'tab') is None:
                continue
            role = 'page' if is_page or run.find(W + 'tab') is not None else 'label'
            rp = run.find(W + 'rPr')
            if rp is not None:
                run.remove(rp)
            run.insert(0, deepcopy(profile[level][role]))
        count += 1
    if not count:
        raise TocError('No supported generated TOC entries were found.')
    if instructions_before != [i.text for i in doc.iter(W + 'instrText')]:
        raise TocError('Field instructions changed unexpectedly.')
    if bookmarks_before != [(n.tag, dict(n.attrib)) for n in doc.iter()
                            if n.tag in {W + 'bookmarkStart', W + 'bookmarkEnd'}]:
        raise TocError('Bookmarks changed unexpectedly.')
    # Retain prefixes referenced only by QName-valued attributes (e.g. mc:Ignorable).
    # ElementTree otherwise drops declarations whose URI has no element/attribute use.
    used_uris = {name[1:].split('}', 1)[0] for node in doc.iter()
                 for name in (node.tag, *node.attrib) if name.startswith('{')}
    for prefix, uri in namespaces.items():
        if uri not in used_uris:
            doc.set('xmlns' + (':' + prefix if prefix else ''), uri)
    parts['word/document.xml'] = ET.tostring(doc, encoding='utf-8', xml_declaration=True)
    # Exclusive creation prevents accidental replacement even after preflight.
    with output.open('xb') as handle:
        with ZipFile(handle, 'w') as zout:
            for info in infos:
                zout.writestr(info, parts[info.filename])
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--profile', type=Path,
                        default=Path(__file__).with_name('builtin_toc_profile.json'),
                        help='Formatting-only profile; default is the built-in format, never infer template choice.')
    args = parser.parse_args()
    try:
        count = restore(args.input, args.output, args.profile)
    except (OSError, ValueError, KeyError, TypeError, AttributeError, BadZipFile, ET.ParseError) as exc:
        # No document text or source paths are printed by default.
        message = str(exc) if isinstance(exc, TocError) else 'Cannot process this file or profile.'
        print('Error: ' + message, file=sys.stderr)
        return 1
    print(f'Restored formatting for {count} TOC entries in a new copy. Check the saved/reopened DOCX in WPS; PDF checks are optional.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
