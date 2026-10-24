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

### 目录更新后的明确修正步骤

将已实测通过的恢复动作写入日常步骤：内置方案完整更新目录后，检查并将偏离的章级页码恢复为 Times New Roman 四号常规，再保存关闭重开确认。只处理偏差，不改变章级标签、其他层级或已对齐位置；自定义模板采用自身格式。本次明确既有方法，无新增实测结论。

### 将已验证修正纳入正常步骤

入口汇总目录字号、静态页眉改名、目录跟踪操作和同名字体补齐的适用处理，区分“软件未自动保持”与“定向修正后满足格式”。不新增实验结论，未覆盖情形不再混同为已发现错误。

### 处理步骤与验证范围统一

README 和入口统一采用检查、定向修正、保存重开确认的正常步骤；入口分别列出已验证方法及未覆盖范围，目录/页眉/字体专项明确历史失败的适用阶段。以当前 DOCX 对象是否实际符合所选格式判定通过，未覆盖实验不预判为错误，XML 辅助、PDF 按需。本次仅整理既有方法与证据，无新增 WPS 实验或格式参数。

### 中文长标题与多页目录实测

独立中性样稿在所记 Mac WPS 中完成完整目录更新、偏差修正、只更新页码、保存关闭及两次磁盘重开；中文两至三行标题、多页三级目录、单双位数页码右对齐、所查跨页边界及三级代表条目跳转有限通过。段中不分页作为实际拆页问题的技术适配单列，未改母版参数。入口、参数表、README 及专项同步区分新增通过范围与剩余未知。无 PDF 导出；未覆盖母版或论文，未公开样稿、截图、路径或字体。

### 长标题与多页目录一致性复查

核对入口、README、参数表和专项：中文长标题/多页目录有限通过范围保持一致，旧阶段状态补充后续定位；“只更新页码”明确以标题及层级未变为前提。条目段中不分页仍为按需技术适配，复杂目录变体及长页眉等未覆盖范围保留。样稿页数、页码和条目数不作为通用规则；本次文档复查未新增实测。

### 前置页编号与正文重启实测

独立中性样稿在所记 Mac WPS 中完成分节编号、整个目录更新、对应格式修正、页码刷新、保存关闭与磁盘重开。所查前置连续大写罗马编号、正文从 1 重启、后续正文延续、目录页码与静态页眉页脚对应及代表链接落点有限通过。源母版未明确页码格式和起始值，实验编号方案单列为任务适配，不补成母版默认要求；复杂前置变体及完整材料仍未覆盖。入口、参数表、README 和专项同步，历史未覆盖表述限定到对应阶段；无 PDF 导出，未公开母版、样稿、截图、个人路径或字体。

本轮公开与本地 skill 结构校验通过；108 处本地 Markdown 链接可解析，共用参考文件核对一致，diff 空白检查及公开文件隐私扫描通过。未改脚本，未新增脚本测试或 PDF 验证结论。

### 无编号封面/声明与后续编号组合

独立中性样稿新增封面和声明占位页，按母版对应段落保留设置，空页脚按节隔离，首个编号前置节恢复 PAGE 页脚并明确编号起点；WPS 完整目录更新、格式恢复、页码刷新及保存关闭磁盘重开后，所查前页无可见页码、前置连续编号、正文重启与延续、目录对应及代表跳转有限通过。编号适配不成为母版默认规则，节数和页数不推广。新增前页仍显示缺字体及云字体提示，保留原声明、具体触发项及实际映射未确认；不称整个样稿全部格式通过。不导出 PDF、不安装字体，未覆盖母版或论文。公开仅同步方法、结果和限制。

本轮公开与本地 skill 结构校验、114 处本地文档链接、共用参考文件一致性、diff 空白检查及公开文件隐私扫描通过。脚本未变，未新增自动化测试或 PDF 验证结论。

### 来源首页校徽图片复用

定位源文件首页的校徽与学院名称组合 PNG，区分规范说明首页与后续学位论文封面示例。独立样稿保留原图、显示尺寸、居中段落及前方排布，经 WPS 保存关闭磁盘重开后，所查尺寸、位置和显示质量有限通过；保存后原图资源保留，同缩放所查图像区域与参考一致。嵌入式类型有来源/保存属性及页面显示证据，但未取得环绕下拉菜单的独立读数，明确记录；打印质量、其他环境和完整封面不扩展为通过。完整参考副本打开超时后改用独立首页参考，不据此声称完整母版通过。无 PDF 导出，未分发原图、DOCX、截图、个人路径或字体。

本轮公开与本地 skill 结构校验、122 处本地链接、共用参考文件一致性、diff 空白及公开文件隐私检查通过；未改公开脚本，未新增自动化测试或 PDF 验证结论。

### 更正封面图像识别并复用实际封面

母版论文封面确有两张独立校名/校徽图像，原先遗漏是未完整遍历说明文本框同段对象；不是母版缺少来源。入口和专项更正，规范首页组合图与实际封面图区分。独立封面保留原图、浮动锚点/上下型环绕、段落及字段；填入短题目按母版明确标注处理，说明占位 run 自身字号不当作填入题目字号。修正后 WPS 保存关闭磁盘重开、所查单页布局及题目字号有限通过，图像资源保留；缺字体实际映射、长题目及打印等范围继续保留。不导出 PDF，不公开 DOCX、原图、个人路径或截图。

本轮公开/本地 skill 结构检查、131 处本地链接、共用参考一致性、diff 空白和公开隐私检查通过。未改公开脚本；未新增 PDF 或字体实际映射通过结论。

## 母版实际设置与明确标注整体复核

本轮静态检查了参考 DOCX 的正文对象、说明框、节、表格、样式、编号、主题及页眉页脚引用。新增[统一复核表](../skills/zju-thesis-format/references/source-format-audit.md)，区分说明自身属性、明确指向待填内容的要求、示例实际设置和采用方式。入口、内置参数、继承说明、提取表及验收记录已同步。

修正遗漏的致谢/中文摘要/附录正文 12 pt、1.5 倍，Abstract 标题 15 pt 加粗，题注 10.5 pt 单倍及通常三线表 0.75 pt；旧示例固定 24 pt、常规标题和 0.5 pt 表线作为实际来源差异记录，不继续充当冲突项的默认。摘要尾部空白与段落标记的 14 pt 不再概括为正文局部字号要求；题注对齐及缩进按对象区分。补录图内文字、流程图、轴标、公式符号、正文引用和分类型书目检查，不引入新字库或无来源补值。页边距不变。

本轮未操作 WPS 或导出 PDF。新增落实项仅完成来源核查，明确保留 WPS 未验证；既有有限实验不被扩大为新配置、完整母版或任意论文通过。源文件保持不变，只公开脱敏属性及方法，不包含原文件、提取原文、私有路径、工作流程、字库或图像。脚本及目录配置未改变。

本次公开仓库本地文档链接 151 处、独立复制安装目录链接 115 处均可解析；项目 skill 的 165 处链接可解析。公开包及项目 skill 结构校验通过，公开变更通过空白检查与定向隐私/文件类型扫描；未发现本机路径、个人论文内容或协作流程，未纳入源文档、字库或图片。GitHub About 与两种用法一致，无需改动。本轮没有修改辅助脚本或运行新的 WPS/渲染实验。

## 明确标注的独立样稿 WPS 往返

后续在 Mac WPS 教育版 12.1.25867 完成中性文字独立样稿的实际另存、菜单关闭回首页、重开保存文件及逐对象面板/页面检查。所查三类正文1.5倍、Abstract 15pt加粗、题注10.5pt单倍、真实单元格0.75pt边线有限通过；英文摘要保持固定24pt。参数、入口与当前验证状态同步更新，原来源差异仍保留。通用文字边框的默认宽度不当作表线；先选实际单元格再读取。其他正文/题注变体、图文相对位置及复杂表格未扩展通过；没有PDF、字库身份或完整母版新结论。仅发布脱敏方法与限定结果，不发布样稿、截图、读取原文、本机路径或字体。

本轮158处仓库本地链接、独立安装副本121处链接、项目skill174处链接均可解析；项目与独立安装skill结构校验通过，公开变更的定向隐私及禁入文件类型扫描无命中。未改变脚本或依赖，不声称重新运行辅助脚本测试。

## 长题注、图文与普通跨页表格往返

在相同Mac WPS版本中另用独立样稿复用对应嵌入式图片原型、中英文题注、表题及两列表格结构，延长中性内容。实际另存、关闭回首页、重开磁盘文件后，所查多行题注五号/单倍、图片上题注下和正文接续、长表题在表上、普通表格的行内跨页续行及末行显示有限通过；行属性允许跨页、表格级边框0.75pt已由界面核对。辅助存盘检查支持文字、行/单元格和图像资源保留；图像尺寸有微小舍入，未为XML数值一致回改实际合格布局。未启用重复表头或自动续表题，没有新增浮动原型、页末绑定或复杂合并表通过结论，没有PDF或新字体身份结论。只发布脱敏方法与有限结果；母版、论文、图像、样稿、截图和私有路径未发布。

本轮公开仓库167处本地链接、独立安装副本129处链接、项目skill182处链接均可解析；skill结构检查、变更空白检查和定向隐私/禁入文件类型扫描通过。未改公开脚本或依赖，不将文档检查冒充新的辅助脚本或渲染实验。

## 浮动图片与页末绑定补充

所查母版紧密环绕浮动原型在普通/页末位置保存关闭重开有限通过；行内图页末分离已复现，以图片与中英文题注局部分页绑定修正后重开通过。不改母版字体、尺寸及环绕；其他浮动修复、复杂组合及超页整体仍未验证。本轮无 PDF；公开内容不含样稿、源图、截图、个人路径或固定样稿页码。

## 重复表头与续表题补充

独立 DOCX 所查普通两列表格重复首行及显式分段续表题完成 WPS 保存关闭重开，续页表头、题注外观、分段行序与末行有限通过。母版没有设置重复表头或提供续题原型，两项明确为技术适配；自动续表题及复杂变体保留未验证。本轮无 PDF，未公开样稿、个人路径或固定分页数据。

## 多行及合并表头补充

独立 DOCX 的两行连续表头及横纵合并三行表头在 WPS 保存关闭重开后，所查续页整组重复、合并外观、数据续接及末行有限通过。保留母版对应字体、列宽及表内段落；新增结构为测试适配，不写成母版默认。其他复杂合并、任意重排和自动续题未验证。本轮无 PDF，未公开源文件、样稿、截图、个人路径或固定页码。

## 自动续题内容变化对照

独立样稿基线、增文、删回均完成更新域、保存关闭重开；分页分界与重复表头响应内容变化，所测 PAGE/PAGEREF 条件候选却未在续页显示续表标识。可见诊断证明 PAGE/简单 IF 已更新，但重复实例的 PAGE 仍显示首处页码；仅记录此候选失败，不概括全部 WPS 能力。当前副本恢复表外题注并显式分段后重开通过，不作为自动方案发布。未加入自动脚本、母版、样稿、截图、个人路径或固定分页数据，无 PDF。

## 文档收尾

精简 README 与 skill 入口，将内置格式、适用的修正方法和剩余限制分开；专项实验正文保留，通过统一验证索引按需读取。可选 PDF/开发检查说明移至 docs/pdf-tools.md。未扩展 WPS 测试，未改变格式参数或扩大既有通过范围；自动续题候选仍未通过，显式修正与自动处理分别表述。

## 精简后最终核对

README、入口、参数表、继承说明及验证索引对照核查；参数数值和实验正文未改。补充安装命令适用的 shell 环境与手动复制方式，参数/继承页统一指向验证索引，并把自动续题尚无通过方案明确限定于所测 Mac WPS 环境。不新增 WPS 实验或通过范围。

## 2026-10-24 字体、字号与颜色属性补核

只读核对字体槽位、主题/样式、普通与复杂文种字号及颜色来源，新增脱敏逐对象属性表。保留节标题宋体等例外，区分说明深灰、主题链接蓝色、显式黑色与未单列颜色；不新增全文刷黑规则。入口、参数表、继承、来源复核与验证索引同步，README保持简洁。无新增WPS实测，不上传源文件、原文清单、图片、字体或本地路径。


## 2026-10-24 字体颜色独立样稿有限复验

已同步姓名字段、宋体节标题及主题链接蓝色的 WPS 保存关闭重开有限结果；日期逐项重开、其他前页对象、精确颜色及实际字库身份继续分列未验证。入口、参数表、继承、来源复核与验证索引采用同一范围。README 保持简洁，不新增测试段落。只同步通用方法和结果边界。


## 2026-10-24 前后置页格式配置

集中录入封面含独立校名/校徽、中文题名页、声明及授权、致谢与作者简历预留的版式、字体、字号和颜色来源。明确图片资源仍需取得、颜色未单列不补黑色、简历正文无原型不造值；既有有限实测与新增属性核对分开。入口、参数表、继承、来源复核与验证索引均已关联，未扩大 WPS 通过范围。


## 2026-10-24 引用标准接入

增加 GB/T 7714—2025 明确选择入口、官方元数据来源及题录/外观分离规则，当时尚未取得标准全文，未新增导出或 WPS 通过结论；全文取得状态已由下述专项核对更新。公开只用通用结构，不附实际项目书目。

## 2026-10-24 正式文献标准专项核对

取得高校学报托管的正式版扫描件，封面与官方元数据一致，按所列条款核对作者、期刊字段、DOI、顺序编码及类型代码。更新母版旧说明的差异表，明确非连续页分隔尚无所查条款的专门依据；只按出版者题录处理具体条目。入口、引用规则、来源复核和验证索引统一；保留未覆盖条款、导出样式及新增WPS验证限制。公开不含实际书目示例、原文件、扫描件、个人路径或字体。

## 2026-10-24 非期刊文献分类著录补核

按正式扫描件核对图书及析出、学位论文、会议录和网站/网页的项目表及格式，补充版本、授予信息、会议出版形态、引用日期与缺失字段处理。区分必备、有则必备及可选，示意结构不作全槽位强制填充；母版外观参数不改。入口、参数表、来源复核和验证索引均关联分类专项；保留未覆盖类型、具体缺项事实及CSL/WPS未测范围。不公开实际书目、源文件、扫描件或个人路径。
