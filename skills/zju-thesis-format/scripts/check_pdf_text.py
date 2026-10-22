#!/usr/bin/env python3
"""Check page/Form font embedding and optional DOCX paragraph presence.

Requires pypdf. Does not replace visual, actual search, glyph, field, equation,
annotation-appearance or pagination review. Reads local files; no network use.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from pypdf import PdfReader

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('pdf', type=Path)
parser.add_argument('--docx', type=Path)
parser.add_argument('--font', help='Optional expected PostScript font name; no default font.')
parser.add_argument('--include-missing-text', action='store_true',
                    help='Opt in to printing unmatched DOCX text; may disclose manuscript content.')
parser.add_argument('--include-source-path', action='store_true',
                    help='Opt in to printing the PDF input path; the default uses the anonymous label input.pdf.')
args = parser.parse_args()
reader = PdfReader(args.pdf)
texts = [page.extract_text() or '' for page in reader.pages]
fonts = {}
seen_resources = set()
seen_fonts = set()


def resolve(value):
    return value.get_object() if hasattr(value, 'get_object') else value


def walk_resources(resources, location):
    resources = resolve(resources)
    if not resources or id(resources) in seen_resources:
        return
    seen_resources.add(id(resources))
    for resource_name, ref in resolve(resources.get('/Font', {})).items():
        font = resolve(ref)
        if id(font) in seen_fonts:
            continue
        seen_fonts.add(id(font))
        descendants = resolve(font.get('/DescendantFonts', [font]))
        for child_index, child_ref in enumerate(descendants):
            child = resolve(child_ref)
            descriptor = resolve(child.get('/FontDescriptor', {}))
            streams = {}
            for key in ('/FontFile', '/FontFile2', '/FontFile3'):
                if key in descriptor:
                    data = resolve(descriptor[key]).get_data()
                    streams[key] = {'bytes': len(data), 'signature_hex': data[:4].hex()}
            name = str(font.get('/BaseFont', child.get('/BaseFont', 'unknown')))
            key = name if name not in fonts else f'{name}#{len(fonts)+1}'
            unicode_stream = resolve(font.get('/ToUnicode'))
            has_mapping = bool(unicode_stream is not None and hasattr(unicode_stream, 'get_data')
                               and unicode_stream.get_data())
            fonts[key] = {'name': name, 'location': f'{location}/{resource_name}/{child_index}',
                          'embedded': any(s['bytes'] for s in streams.values()),
                          'to_unicode': has_mapping, 'streams': streams}
    for resource_name, ref in resolve(resources.get('/XObject', {})).items():
        obj = resolve(ref)
        if obj.get('/Subtype') == '/Form':
            walk_resources(obj.get('/Resources', {}), f'{location}/{resource_name}')


for number, page in enumerate(reader.pages, 1):
    walk_resources(page.get('/Resources', {}), f'page{number}')


def compact(text):
    return re.sub(r'\s+', '', text)


missing = []
paragraph_count = 0
if args.docx:
    with ZipFile(args.docx) as archive:
        root = ET.fromstring(archive.read('word/document.xml'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    extracted = compact('\n'.join(texts))
    for paragraph in root.findall('.//w:body//w:p', ns):
        text = ''.join(node.text or '' for node in paragraph.findall('.//w:t', ns))
        if compact(text):
            paragraph_count += 1
            if compact(text) not in extracted:
                item = {'nonempty_paragraph_index': paragraph_count, 'characters': len(text)}
                if args.include_missing_text:
                    item['text'] = text
                missing.append(item)
font_present = any(args.font in f['name'] for f in fonts.values()) if args.font else None
paragraphs_passed = not args.docx or (paragraph_count > 0 and not missing)
passed = bool(fonts) and (font_present is not False) and paragraphs_passed and all(
    f['embedded'] and f['to_unicode'] for f in fonts.values())
print(json.dumps({
    'pdf': str(args.pdf) if args.include_source_path else 'input.pdf',
    'sha256': hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
    'pages': len(texts), 'fonts': fonts, 'expected_font_present': font_present,
    'page_text_characters': list(map(len, texts)),
    'docx_paragraphs_checked': paragraph_count,
    'missing_paragraphs': missing, 'passed': passed,
    'limits': 'Page and nested Form resources; embedding/mapping presence, not font-stream '
              'validity or mapping correctness. Optional whitespace-insensitive paragraph '
              'presence, not full glyph/order/visual/search/field/annotation validation.'
}, ensure_ascii=False, indent=2))
raise SystemExit(0 if passed else 1)
