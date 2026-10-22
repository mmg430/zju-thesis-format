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
