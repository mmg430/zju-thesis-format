# Distribution verification — 2026-10-23

Maintainer checks for the public package, not external certification.

## Names and formatting sources

The Chinese display name is **浙江大学研究生论文排版**, the English name is **ZJU Thesis Format**, and the identifier is `zju-thesis-format`. College information is used only to identify the formatting reference: “浙江大学工程师学院研究生论文 DOCX 格式母版”. No official status or current applicability is claimed.

The package supports two modes: apply the [built-in parameters](../skills/zju-thesis-format/references/builtin-format.md), or extract a separately selected DOCX template. Custom-template mode does not overlay built-in values. Unspecified properties are recorded as gaps; a parameter table is not a complete source-template clone.

## File and license checks

The public files are reviewed for unintended personal identifiers, local paths, research content and document-specific process descriptions. No original DOCX/PDF, font, screenshot or private log is included. Root and installable MIT licenses match; the fixed zjuthesis MIT notice and historical Zhuque attribution are retained. Font embedding flags do not establish use or redistribution rights.

## Installation and helper tests

Local document links and the skill structure are checked in the repository and after independent copying. Nine neutral synthetic PDF-helper tests cover Chinese extraction, nested Form fonts, equal-name font objects, default redaction, explicit text opt-in, empty DOCX rejection and optional expected-font checks. Their synthetic font stream tests resource-presence logic, not font validity or WPS rendering.

Without `--font`, the helper does not assume a particular font. It checks embedding-stream and mapping presence, not their correctness, real reader search or complete visual output. Recheck actual target documents independently.

The distribution review inspected all tracked files and reachable historical blobs. The README copy command was reproduced in an isolated consumer directory; local links remained inside the copied skill. A fresh virtual environment installed only the published requirements, and all nine synthetic checks passed with a reduced environment. Seven distinct external reference URLs returned HTTP 200 at check time; availability may change. README anchors and GitHub Markdown rendering were checked. Font guidance now explicitly distinguishes built-in parameters from custom-template declarations.

## Evidence boundary

Built-in formatting values were checked against source DOCX properties. Limited WPS results and failures remain in the [font verification record](../skills/zju-thesis-format/references/font-validation-2026-10-23.md). The source artifacts are not distributed and cannot be independently rechecked from this package. No new WPS rendering, full-document, cross-platform, printing or PDF/A validation is claimed by these distribution checks.

## Skill behavior and inheritance update

The built-in parameter table now links to an attribute-only inheritance reference. It distinguishes document defaults, paragraph and character styles, numbering, direct paragraph settings, paragraph-mark properties and visible text runs. Twenty targeted source-property assertions passed; the source file remained unchanged. Localized mixed sizes, TOC tab stops, table overrides, bibliography numbering and header/footer layers are recorded without source text, fixed pagination or source artifacts.

Read-only inspection no longer selects or applies the built-in format implicitly. Font diagnosis proceeds through text objects, style/numbering chains, defaults/themes and other declarations. Courier and Courier New are distinguished; Japanese theme mappings are candidates, not evidence that those fonts must be installed. Diagnostic deletion is not presented as a format-preserving repair.

Validation now distinguishes XML inspection, saved DOCX changes, WPS roundtrips and PDF output. At that documentation-only stage, no new WPS experiment had been performed. Bibliography indentation was subsequently tested as recorded below; automatic TOC was still untested at that stage (see the later experiment below); dynamic chapter headers and newly discussed font-warning candidates retain their stated unverified scope.

All 24 public files were scanned for private paths, source-document identifiers and personal process wording; no source documents, fonts or images were included. The repository's 56 local document links and the independently copied skill's 34 local links resolved; the copied skill passed the structure validator. Existing helper scripts and dependencies were unchanged, so this documentation update does not claim a new helper-test run.

## Bibliography indentation roundtrip

A subsequent independent neutral sample tested the original bibliography paragraph style, numbering level and direct indentation together in Mac WPS 12.1.25867. Save As, confirmed tab closure, disk reopen and normal PDF export completed. Twelve reference paragraphs retained their relevant properties after style-ID remapping; PDF first-text and continuation starts were 21 points to the right of the body left edge. Baseline and reopened output had identical page renders at 1800-pixel page height. Reader search returned the expected twelve matches.

Only this combination and tested single/two-digit numbering scope are marked passed in the [specialized record](../skills/zju-thesis-format/references/bibliography-indent-validation.md). This does not establish a universal indent precedence or authorize flattening the original settings. Automatic TOC was not tested in that bibliography experiment; its subsequent results are recorded below. Dynamic chapter headers and other uncovered behaviors remain unverified. No source documents, local artifacts, screenshots, private paths or font files are published with this update.

For this roundtrip update, all 25 public files passed the privacy scan, 63 repository-local links and 39 independently copied skill links resolved, and the copied skill passed its structure validator. Original source files and experiment evidence remain local.

## Static chapter-header mapping roundtrip

A subsequent Mac WPS 12.1.25867 experiment reused the source's static header structure in three neutral chapters with first and continuation pages. Baseline and saved/reopened PDFs had identical renders across all pages at 1400-pixel page height. A title-only rename control retained the old header text. Updating only the target section's resolved header part, followed by Save As, confirmed closure, disk reopen and export, changed only the intended chapter-header glyph region; other chapters remained unchanged.

The [specialized record](../skills/zju-thesis-format/references/chapter-header-validation.md) marks static section mapping and targeted update passed within this scope. Automatic title following is absent in the tested static structure; STYLEREF, long names, shared-header splitting and other untested variants remain unverified. Section/header properties, page geometry, PAGE output, embedded-resource presence and actual reader search were checked. WPS's explicit serialization additions are recorded rather than described as byte-identical XML. No local artifacts or private identifiers are published.

For the static-header update, all 26 public files passed the privacy scan, 70 repository-local links and 45 independently copied skill links resolved, and the copied skill passed the structure validator. No helper script or dependency was changed by this documentation update.

## Automatic TOC adaptation roundtrip

A subsequent independent neutral sample in Mac WPS 12.1.25867 tested three heading levels, title changes, an added entry and a pagination change. The source has manual TOC entries; the new TOC field, derived styles and selected subsection outline levels are explicitly technical adaptations. Only-page updating retained stale labels and omitted the new entry. Entire updating collected the correct entries but changed source tab and character properties, so native format retention failed.

The [specialized record](../skills/zju-thesis-format/references/automatic-toc-validation.md) documents restoration after updating, including the complete PAGEREF field carrier range. Setting only result text failed to retain the mixed chapter-page typography. The corrected copy completed Save As, confirmed closure, disk reopen and PDF export. All five before/after renders matched at 1600-pixel page height. Ten entries, their twenty row/page links and the three-level PDF outline had correct target pages; three levels were clicked in the PDF reader. Actual reader search found the expected TOC/body pair. DOCX field references resolved, but precise WPS click landing was not reliably confirmed in that initial experiment; the follow-up below supplies interaction evidence. Resource embedding and ToUnicode presence do not certify every glyph.

Future entire updates may overwrite restored formatting. Multiline or multipage TOCs, front-matter numbering variants, figure/table catalogs, other environments and full-document acceptance are not covered. Source artifacts remained local and unchanged; this update publishes only attribute-level methods and bounded results.

For this update, all 27 public files passed the privacy scan, 81 repository-local links and 54 independently copied skill links resolved, and the copied skill passed the structure validator. Reachable historical blobs were also scanned for private paths and process wording without findings. No helper script or dependency changed; no new helper-test run is claimed.

## DOCX TOC click follow-up

A fresh independent copy retained the existing TOC/HYPERLINK/PAGEREF fields, bookmarks and source-derived typography. No hyperlink rewrite, font substitution or global WPS setting change was needed. After Save As, confirmed closure and disk reopen in the same Mac WPS version, Command-clicking a label and its right-side page number at each of three heading levels reached the exact corresponding heading. Selecting the destination heading line confirmed the landing. Only these six interaction cases are marked passed; plain clicks and other settings/platforms are not established, and the sole cause of the earlier instability was not isolated.

The document XML remained identical apart from the session navigation bookmark; styles, themes and font table were unchanged, with only an additional settings rsid. The exported PDF matched all five prior validated page renders at 1600-pixel height. All twenty PDF row/page links and the three-level outline had correct destinations; three levels were clicked in the reader and the expected TOC/body search pair was found. The native entire-update formatting failure and other untested TOC variants remain unchanged. See the [bounded record](../skills/zju-thesis-format/references/automatic-toc-validation.md). No source artifacts, local paths or screenshots are distributed.

For this click follow-up, all 27 public files passed the targeted privacy scan; 82 repository-local links and 54 independently copied skill links resolved. The independent copy passed the skill structure validator. No helper script or dependency changed; no new helper-test run is claimed.

## Repeatable TOC restoration after entire updates

A subsequent baseline control and a TOC MERGEFORMAT control both retained the formatting failure: WPS generated an 8300-twip right tab and cleared the source-derived 6141-twip tab. This does not establish that every possible native setting is ineffective; the tested controls failed.

The new standard-library restoration helper and formatting-only built-in profile were exercised after two complete native updates. The second cycle renamed a neutral chapter, added an entry and changed pagination; the helper handled the new row without fixed entry counts, labels or page values. It preserved instructions, bookmarks, non-entry paragraphs and all other package parts. Both restored copies completed WPS Save As, confirmed closure, disk reopen and normal PDF export. Source tab/indent/spacing and mixed page-digit typography were checked after WPS rewriting; both PDFs had correct cached pages, links, three-level outlines and embedded-resource presence. The first cycle matched the prior same-input page renders; the second checked changed content and destinations rather than claiming pixel identity with an older document. The new entry was clicked in DOCX and PDF, and real reader search found its TOC/body pair.

Four new neutral OOXML tests cover restoration and non-target preservation, existing-output/same-path rejection, unbalanced fields and uncovered levels; all thirteen helper tests passed. These synthetic checks are separate from the recorded WPS experiments. The helper also preserves original namespace declarations referenced only by compatibility attributes. Its final output completed an additional save/close/reopen/export; all six renders matched the earlier second-cycle output, and the new PDF link/search passed again. Native one-click retention remains failed, and arbitrary repetition, long/multiple-page TOCs, custom profiles and other environments remain unverified. Only format properties, code and sanitized summaries are distributed.

For this restoration-tool update, all 30 public files passed the targeted privacy scan; 84 repository-local links and 56 independently copied skill links resolved. The copied skill passed structure validation, all thirteen tests passed against it, and its helper reproduced the exact final restored document XML from outside the repository. Source samples and verification artifacts remain private.

## DOCX 验收重点调整

统一入口、参数表、使用示例、界面提示及验证方法：以所选母版对应格式在 WPS 中保存重开后的实际显示与功能为准。XML 用于必要的属性提取与问题排查，不要求结构或字节一致；PDF 仅按导出、提交或输出诊断需要另查。历史实测保留原范围，未新增 WPS 或 PDF 实测通过结论；未做 PDF 检查不否定已通过的 DOCX 对象。脚本、参数数值和既有失败项不因本次说明调整而改变。

本次为文档及入口元数据调整，未修改脚本或参数值；skill 结构校验和 diff 空白检查通过，90 处本地文档链接可解析。公开文件扫描未发现敏感信息，未纳入 DOCX、PDF、字库或截图。本次未启动 WPS 或新增渲染实验。

### DOCX 优先原则的残留复查

清理目录复用步骤中“重复输出验收”的泛化要求，改为 WPS 中先查格式与功能、有偏差再修复；字体诊断仅针对实际问题展开，PDF 字段按需记录。继承表明确不是 XML 一致性清单，README 明确 DOCX 检查无须 PDF 依赖。历史实验结果原样保留其证据范围，未新增实测结论，未改参数或脚本。

### 自动目录 DOCX 专项复验

独立样稿完成原生完整更新、保存关闭重开及母版副本画面对照，确认章级页码字号偏差；保留已对齐定位、定向恢复字符格式后，WPS 保存关闭重开与所查实际显示、小节跳转有限通过。本轮不导出 PDF、不比较 XML 一致性。补充手工引导符可见宽度与已设制表位的区别，默认恢复工具不应无差别改写已合格位置。仅公开方法与有限结果，不公开母版、样稿、截图、个人路径或字体。恢复脚本仅调整成功提示，明确 PDF 按需。
