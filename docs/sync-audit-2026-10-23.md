# Distribution verification — 2026-10-23

Maintainer checks for the public package, not external certification.

## Names and formatting sources

The Chinese display name is **浙江大学研究生论文排版**, the English name is **ZJU Thesis Format**, and the identifier is `zju-thesis-format`. College information is used only to identify the formatting reference: “浙江大学工程师学院研究生论文 DOCX 格式母版”. No official status or current applicability is claimed.

The package supports two modes: apply the [built-in parameters](../skills/zju-thesis-format/references/builtin-format.md), or extract a separately selected DOCX template. Custom-template mode does not overlay built-in values. Unspecified properties are recorded as gaps; a parameter table is not a complete source-template clone.

## File and license checks

The public files are reviewed for unintended personal identifiers, local paths, research content and document-specific process descriptions. No original DOCX/PDF, font, screenshot or private log is included. Root and installable MIT licenses match; the fixed zjuthesis MIT notice and historical Zhuque attribution are retained. Font embedding flags do not establish use or redistribution rights.

## Installation and helper tests

Local document links and the skill structure are checked in the repository and after independent copying. Nine neutral synthetic tests cover Chinese extraction, nested Form fonts, equal-name font objects, default redaction, explicit text opt-in, empty DOCX rejection and optional expected-font checks. Their synthetic font stream tests resource-presence logic, not font validity or WPS rendering.

Without `--font`, the helper does not assume a particular font. It checks embedding-stream and mapping presence, not their correctness, real reader search or complete visual output. Recheck actual target documents independently.

The distribution review inspected all tracked files and reachable historical blobs. The README copy command was reproduced in an isolated consumer directory; local links remained inside the copied skill. A fresh virtual environment installed only the published requirements, and all nine synthetic checks passed with a reduced environment. Seven distinct external reference URLs returned HTTP 200 at check time; availability may change. README anchors and GitHub Markdown rendering were checked. Font guidance now explicitly distinguishes built-in parameters from custom-template declarations.

## Evidence boundary

Built-in formatting values were checked against source DOCX properties. Limited WPS results and failures remain in the [font verification record](../skills/zju-thesis-format/references/font-validation-2026-10-23.md). The source artifacts are not distributed and cannot be independently rechecked from this package. No new WPS rendering, full-document, cross-platform, printing or PDF/A validation is claimed by these distribution checks.

## Skill behavior and inheritance update

The built-in parameter table now links to an attribute-only inheritance reference. It distinguishes document defaults, paragraph and character styles, numbering, direct paragraph settings, paragraph-mark properties and visible text runs. Twenty targeted source-property assertions passed; the source file remained unchanged. Localized mixed sizes, TOC tab stops, table overrides, bibliography numbering and header/footer layers are recorded without source text, fixed pagination or source artifacts.

Read-only inspection no longer selects or applies the built-in format implicitly. Font diagnosis proceeds through text objects, style/numbering chains, defaults/themes and other declarations. Courier and Courier New are distinguished; Japanese theme mappings are candidates, not evidence that those fonts must be installed. Diagnostic deletion is not presented as a format-preserving repair.

Validation now distinguishes XML inspection, saved DOCX changes, WPS roundtrips and PDF output. At that documentation-only stage, no new WPS experiment had been performed. Bibliography indentation was subsequently tested as recorded below; automatic TOC setup, dynamic chapter headers and newly discussed font-warning candidates retain their stated unverified scope.

All 24 public files were scanned for private paths, source-document identifiers and personal process wording; no source documents, fonts or images were included. The repository's 56 local document links and the independently copied skill's 34 local links resolved; the copied skill passed the structure validator. Existing helper scripts and dependencies were unchanged, so this documentation update does not claim a new helper-test run.

## Bibliography indentation roundtrip

A subsequent independent neutral sample tested the original bibliography paragraph style, numbering level and direct indentation together in Mac WPS 12.1.25867. Save As, confirmed tab closure, disk reopen and normal PDF export completed. Twelve reference paragraphs retained their relevant properties after style-ID remapping; PDF first-text and continuation starts were 21 points to the right of the body left edge. Baseline and reopened output had identical page renders at 1800-pixel page height. Reader search returned the expected twelve matches.

Only this combination and tested single/two-digit numbering scope are marked passed in the [specialized record](../skills/zju-thesis-format/references/bibliography-indent-validation.md). This does not establish a universal indent precedence or authorize flattening the original settings. Automatic TOC, dynamic chapter headers and other uncovered behaviors remain unverified. No source documents, local artifacts, screenshots, private paths or font files are published with this update.

For this roundtrip update, all 25 public files passed the privacy scan, 63 repository-local links and 39 independently copied skill links resolved, and the copied skill passed its structure validator. Original source files and experiment evidence remain local.

## Static chapter-header mapping roundtrip

A subsequent Mac WPS 12.1.25867 experiment reused the source's static header structure in three neutral chapters with first and continuation pages. Baseline and saved/reopened PDFs had identical renders across all pages at 1400-pixel page height. A title-only rename control retained the old header text. Updating only the target section's resolved header part, followed by Save As, confirmed closure, disk reopen and export, changed only the intended chapter-header glyph region; other chapters remained unchanged.

The [specialized record](../skills/zju-thesis-format/references/chapter-header-validation.md) marks static section mapping and targeted update passed within this scope. Automatic title following is absent in the tested static structure; STYLEREF, long names, shared-header splitting and other untested variants remain unverified. Section/header properties, page geometry, PAGE output, embedded-resource presence and actual reader search were checked. WPS's explicit serialization additions are recorded rather than described as byte-identical XML. No local artifacts or private identifiers are published.

For the static-header update, all 26 public files passed the privacy scan, 70 repository-local links and 45 independently copied skill links resolved, and the copied skill passed the structure validator. No helper script or dependency was changed by this documentation update.
