"""Synthetic PDF/DOCX checks; no thesis, WPS or private project inputs."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

from pypdf import PdfWriter
from pypdf.generic import (ArrayObject, DecodedStreamObject, DictionaryObject,
                          FloatObject, NameObject, NumberObject)

SKILL = Path(os.environ.get('ZJU_SKILL_PATH', Path(__file__).resolve().parents[1] / 'skills/zju-thesis-format'))
SCRIPT = SKILL / 'scripts/check_pdf_text.py'
# Presence-only synthetic stream; not a renderable font or redistributed font binary.
FONT_STREAM = b'SYNTHETIC_FONT_STREAM_FOR_RESOURCE_PRESENCE_TEST'


def font(writer, embedded=True):
    desc = DictionaryObject({NameObject('/Type'): NameObject('/FontDescriptor'),
        NameObject('/FontName'): NameObject('/SyntheticAuditFont'),
        NameObject('/Flags'): NumberObject(4),
        NameObject('/FontBBox'): ArrayObject([NumberObject(x) for x in [0, -200, 1000, 1000]]),
        NameObject('/ItalicAngle'): NumberObject(0), NameObject('/Ascent'): NumberObject(800),
        NameObject('/Descent'): NumberObject(-200), NameObject('/CapHeight'): NumberObject(700),
        NameObject('/StemV'): NumberObject(80)})
    if embedded:
        stream = DecodedStreamObject(); stream.set_data(FONT_STREAM)
        desc[NameObject('/FontFile2')] = writer._add_object(stream)
    cmap = DecodedStreamObject()
    cmap.set_data(b'/CIDInit /ProcSet findresource begin 12 dict begin begincmap\n'
        b'/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n'
        b'/CMapName /Synthetic-UCS def /CMapType 2 def\n'
        b'1 begincodespacerange <00> <FF> endcodespacerange\n'
        b'1 beginbfchar <41> <4E2D> endbfchar\nendcmap end end')
    return writer._add_object(DictionaryObject({NameObject('/Type'): NameObject('/Font'),
        NameObject('/Subtype'): NameObject('/TrueType'),
        NameObject('/BaseFont'): NameObject('/SyntheticAuditFont'),
        NameObject('/FirstChar'): NumberObject(65), NameObject('/LastChar'): NumberObject(65),
        NameObject('/Widths'): ArrayObject([NumberObject(600)]),
        NameObject('/FontDescriptor'): writer._add_object(desc),
        NameObject('/ToUnicode'): writer._add_object(cmap)}))


def pdf(path, mode='normal'):
    writer = PdfWriter(); good = font(writer)
    page = writer.add_blank_page(200, 200)
    page[NameObject('/Resources')] = DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F1'): good})})
    content = DecodedStreamObject(); content.set_data(b'BT /F1 12 Tf 20 100 Td (A) Tj ET')
    page[NameObject('/Contents')] = writer._add_object(content)
    if mode == 'form-unembedded':
        bad = font(writer, embedded=False); form = DecodedStreamObject()
        form.set_data(b'BT /F2 12 Tf 20 60 Td (A) Tj ET')
        form.update({NameObject('/Type'): NameObject('/XObject'), NameObject('/Subtype'): NameObject('/Form'),
            NameObject('/BBox'): ArrayObject([FloatObject(x) for x in [0, 0, 200, 200]]),
            NameObject('/Resources'): DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F2'): bad})})})
        page['/Resources'][NameObject('/XObject')] = DictionaryObject({NameObject('/Fm'): writer._add_object(form)})
        content.set_data(b'BT /F1 12 Tf 20 100 Td (A) Tj ET /Fm Do')
    elif mode == 'name-collision':
        page['/Resources']['/Font'][NameObject('/F1')] = font(writer, embedded=False)
        page2 = writer.add_blank_page(200, 200)
        page2[NameObject('/Resources')] = DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F1'): good})})
        page2[NameObject('/Contents')] = writer._add_object(content)
    writer.write(path)


class CheckPdfTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name)
    def tearDown(self):
        self.tmp.cleanup()
    def run_check(self, mode='normal', *args):
        target = self.root/'sample.pdf'; pdf(target, mode)
        result = subprocess.run([sys.executable, '-I', str(SCRIPT), str(target), *args],
                                cwd=self.root, capture_output=True, text=True)
        return result, json.loads(result.stdout)
    def docx(self, text):
        path = self.root/'sample.docx'
        with ZipFile(path, 'w') as z:
            z.writestr('word/document.xml', '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>'+text+'</w:t></w:r></w:p></w:body></w:document>')
        return path
    def test_embedded_chinese_text(self):
        result, report = self.run_check('normal', '--docx', str(self.docx('中')))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(report['passed']); self.assertEqual(report['docx_paragraphs_checked'], 1)
    def test_unembedded_font_inside_form_is_rejected(self):
        result, report = self.run_check('form-unembedded')
        self.assertEqual(result.returncode, 1); self.assertFalse(report['passed'])
    def test_equal_font_names_do_not_hide_unembedded_object(self):
        result, report = self.run_check('name-collision')
        self.assertEqual(result.returncode, 1); self.assertFalse(report['passed'])
    def test_missing_text_is_redacted_by_default(self):
        private = 'SYNTHETIC_UNMATCHED_TEST_PARAGRAPH'
        result, report = self.run_check('normal', '--docx', str(self.docx(private)))
        self.assertEqual(result.returncode, 1); self.assertNotIn(private, result.stdout)
        self.assertEqual(len(report['missing_paragraphs']), 1)

    def test_source_path_is_redacted_by_default(self):
        result, report = self.run_check()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(report['pdf'], 'input.pdf')
        self.assertNotIn('sample.pdf', result.stdout)
        self.assertNotIn(str(self.root), result.stdout)
    def test_missing_text_requires_explicit_opt_in(self):
        text = 'SYNTHETIC_DIAGNOSTIC_ONLY'
        result, report = self.run_check('normal', '--docx', str(self.docx(text)), '--include-missing-text')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(report['missing_paragraphs'][0]['text'], text)
    def test_no_font_default_accepts_document_specific_font(self):
        result, report = self.run_check()
        self.assertEqual(result.returncode, 0)
        self.assertIsNone(report['expected_font_present'])
    def test_explicit_expected_font_is_enforced(self):
        result, report = self.run_check('normal', '--font', 'AbsentFont')
        self.assertEqual(result.returncode, 1)
        self.assertFalse(report['expected_font_present'])
    def test_empty_docx_is_not_content_success(self):
        result, report = self.run_check('normal', '--docx', str(self.docx('')))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(report['docx_paragraphs_checked'], 0)


if __name__ == '__main__':
    unittest.main()
