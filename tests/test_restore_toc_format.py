"""Neutral OOXML checks; actual WPS results are recorded separately."""
import hashlib
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile
import xml.etree.ElementTree as E

SKILL = Path(os.environ.get('ZJU_SKILL_PATH', Path(__file__).resolve().parents[1] / 'skills/zju-thesis-format'))
SPEC = importlib.util.spec_from_file_location('toc_restore', SKILL / 'scripts/restore_toc_format.py')
TOC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOC)
W = TOC.W
E.register_namespace('mc', 'http://schemas.openxmlformats.org/markup-compatibility/2006')
PROFILE = SKILL / 'scripts/builtin_toc_profile.json'


def run(p, tag, text=None, **attributes):
    r = E.SubElement(p, W + 'r')
    n = E.SubElement(r, W + tag, {W + k: v for k, v in attributes.items()})
    n.text = text
    return r


def fixture(path, levels=(1, 2, 3, 2), malformed=False):
    doc = E.Element(W + 'document'); doc.set('xmlns:w14', 'urn:neutral-word-extension'); doc.set('{http://schemas.openxmlformats.org/markup-compatibility/2006}Ignorable', 'w14'); body = E.SubElement(doc, W + 'body')
    for i, level in enumerate(levels):
        p = E.SubElement(body, W + 'p'); pp = E.SubElement(p, W + 'pPr')
        E.SubElement(pp, W + 'pStyle', {W + 'val': 'mapped-' + str(level)})
        tabs = E.SubElement(pp, W + 'tabs')
        E.SubElement(tabs, W + 'tab', {W + 'val': 'right', W + 'pos': '8300'})
        if i == 0:
            run(p, 'fldChar', fldCharType='begin'); run(p, 'instrText', ' TOC \\o "1-3" \\h ')
            run(p, 'fldChar', fldCharType='separate')
        run(p, 'fldChar', fldCharType='begin'); run(p, 'instrText', f' HYPERLINK \\l anchor{i} ')
        run(p, 'fldChar', fldCharType='separate'); run(p, 't', f'Entry {i}'); run(p, 'tab')
        run(p, 'fldChar', fldCharType='begin'); run(p, 'instrText', f' PAGEREF anchor{i} \\h ')
        run(p, 'fldChar', fldCharType='separate'); run(p, 't', str(20 + i))
        run(p, 'fldChar', fldCharType='end'); run(p, 'fldChar', fldCharType='end')
        if i == len(levels) - 1 and not malformed:
            run(p, 'fldChar', fldCharType='end')
    for i, level in enumerate(levels):
        p = E.SubElement(body, W + 'p')
        E.SubElement(p, W + 'bookmarkStart', {W + 'id': str(i), W + 'name': f'anchor{i}'})
        run(p, 't', f'Entry {i}')
        E.SubElement(p, W + 'bookmarkEnd', {W + 'id': str(i)})
    # A same-style PAGEREF outside the actual TOC must remain untouched.
    p = E.SubElement(body, W + 'p'); pp = E.SubElement(p, W + 'pPr')
    E.SubElement(pp, W + 'pStyle', {W + 'val': 'mapped-1'})
    run(p, 'fldChar', fldCharType='begin'); run(p, 'instrText', ' PAGEREF anchor0 \\h ')
    run(p, 'fldChar', fldCharType='separate'); run(p, 't', '20'); run(p, 'fldChar', fldCharType='end')
    styles = E.Element(W + 'styles')
    for level in set(levels):
        st = E.SubElement(styles, W + 'style', {W + 'styleId': 'mapped-' + str(level)})
        E.SubElement(st, W + 'name', {W + 'val': 'toc ' + str(level)})
    with ZipFile(path, 'w') as z:
        z.writestr('word/document.xml', E.tostring(doc))
        z.writestr('word/styles.xml', E.tostring(styles))
        z.writestr('word/theme/theme1.xml', b'<theme/>')
    return doc


class RestoreTocTests(unittest.TestCase):
    def test_restores_variable_entries_and_preserves_non_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory); source = p / 'input.docx'; output = p / 'output.docx'
            before = fixture(source); digest = hashlib.sha256(source.read_bytes()).digest()
            self.assertEqual(TOC.restore(source, output, PROFILE), 4)
            self.assertEqual(hashlib.sha256(source.read_bytes()).digest(), digest)
            with ZipFile(source) as a, ZipFile(output) as b:
                self.assertIn(b'xmlns:w14="urn:neutral-word-extension"', b.read('word/document.xml'))
                after = E.fromstring(b.read('word/document.xml'))
                for name in a.namelist():
                    if name != 'word/document.xml': self.assertEqual(a.read(name), b.read(name))
            self.assertEqual([i.text for i in before.iter(W + 'instrText')], [i.text for i in after.iter(W + 'instrText')])
            self.assertEqual([dict(i.attrib) for i in before.iter(W + 'bookmarkStart')], [dict(i.attrib) for i in after.iter(W + 'bookmarkStart')])
            self.assertEqual(E.tostring(before.find(W + 'body')[-1]), E.tostring(after.find(W + 'body')[-1]))
            row = after.find(W + 'body')[0]
            self.assertEqual(row.find('.//' + W + 'tab').get(W + 'pos'), '6141')
            rr = next(r for r in row.iter(W + 'r') if any('PAGEREF' in (n.text or '') for n in r.findall(W + 'instrText')))
            self.assertEqual(rr.find(W + 'rPr/' + W + 'sz').get(W + 'val'), '28')
            self.assertEqual(rr.find(W + 'rPr/' + W + 'b').get(W + 'val'), '0')
            # A second restoration is formatting-idempotent, independent of the cache digits.
            TOC.restore(output, p / 'again.docx', PROFILE)
            with ZipFile(output) as a, ZipFile(p / 'again.docx') as b:
                self.assertEqual(a.read('word/document.xml'), b.read('word/document.xml'))

    def test_refuses_overwrite_and_same_path(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory); source = p / 'input.docx'; fixture(source)
            output = p / 'existing.docx'; output.write_bytes(b'keep')
            for dest in (source, output):
                with self.assertRaises(TOC.TocError): TOC.restore(source, dest, PROFILE)
            self.assertEqual(output.read_bytes(), b'keep')

    def test_unbalanced_fields_do_not_create_output(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory); source = p / 'bad.docx'; fixture(source, malformed=True)
            with self.assertRaises(TOC.TocError): TOC.restore(source, p / 'output.docx', PROFILE)
            self.assertFalse((p / 'output.docx').exists())

    def test_uncovered_level_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory); source = p / 'level4.docx'; fixture(source, levels=(4,))
            with self.assertRaises(TOC.TocError): TOC.restore(source, p / 'output.docx', PROFILE)
            self.assertFalse((p / 'output.docx').exists())


if __name__ == '__main__': unittest.main()
