<div align="center">

# ZJU Thesis Format

**浙江大学研究生论文排版**

<a href="LICENSE"><kbd>MIT License</kbd></a> &nbsp;
<a href="skills/zju-thesis-format/references/builtin-format.md"><kbd>内置排版方案</kbd></a> &nbsp;
<a href="skills/zju-thesis-format/references/wps-profile.md"><kbd>自定义模板</kbd></a>

[项目简介](#overview) · [两种用法](#usage) · [安装](#install) · [文档与工具](#resources) · [来源与许可](#sources)

</div>

---

<a id="overview"></a>
## 项目简介

面向浙江大学的研究生论文排版与核验工具。内置排版方案参考**浙江大学工程师学院研究生论文 DOCX 格式**。

你可以直接使用仓库中已有的排版参数，也可以提供自己的 DOCX 模板，通过同一套方法提取格式、建立新的排版配置。支持页面、标题、正文、图表、目录和参考文献的格式处理，以 DOCX 在 WPS 中保存重开后的实际格式为验收重点；XML 辅助排查，PDF 按需检查。

<a id="usage"></a>
## 两种用法

| 用法 | 需要准备 | 格式依据 |
| :--- | :--- | :--- |
| **直接使用内置方案** | 需要排版的文档 | 仓库已包含的[排版参数](skills/zju-thesis-format/references/builtin-format.md)，无需另行提供源母版 |
| **使用自定义模板** | 自己的 DOCX 模板和目标文档 | 提取模板对应对象的实际设置及明确格式标注，建立新配置，不叠加内置参数 |

仅检查现有文档时保持只读，不自动应用任何方案；排版修改按明确选定的格式执行。

### 直接使用内置方案

```text
使用 $zju-thesis-format，按内置排版方案处理文档。
目标文档：<DOCX 路径>
在副本上应用已记录的页面、标题、正文、图表及书目参数。
未记录项保留原设置并说明；完成后在 WPS 中保存重开，核对 DOCX 实际格式；PDF 按需检查。
```

内置参数可直接查阅，包括页边距、字体、字号、行距和段距等。它是可复用的格式配置，不包含完整 DOCX 母版；样式、编号和直接格式的已知关系见[继承说明](skills/zju-thesis-format/references/builtin-inheritance.md)，未列属性保留并标明。

### 使用自定义模板

```text
使用 $zju-thesis-format，以我提供的模板建立排版配置。
模板：<模板 DOCX 路径>
目标文档：<目标 DOCX 路径>
逐对象提取实际设置及明确格式标注，保留字体、样式继承和段内差异。
不套用内置参数；在副本上完成排版，在 WPS 中保存重开并核对 DOCX 实际格式。
XML 仅辅助排查，PDF 按需检查。
```

### 排版与检查

应用所选格式 → 在 WPS 中检查 → 修正实际偏差 → 保存、关闭重开确认。**修正后满足母版格式，即可判定所查 DOCX 对象通过。**

目录更新后的字号恢复、章名改变后的静态页眉同步、对应原字体补齐等，均作为正常处理步骤，见 [skill 的处理方法](skills/zju-thesis-format/SKILL.md#常见偏差的处理)。无需等待软件自动保持全部格式；已合格的位置也不因 XML 表示不同而改动。PDF 仅按需检查。目录修正后若标题和层级未变，只刷新页码，再保存重开核对；样稿页数、起页和条目数均不作为规则。

<a id="install"></a>
## 安装

将完整 skill 目录复制到目标项目：

```sh
git clone https://github.com/mmg430/zju-thesis-format.git
cd zju-thesis-format

# 替换为你的项目目录
mkdir -p /path/to/your-project/.agents/skills
cp -R skills/zju-thesis-format /path/to/your-project/.agents/skills/
```

助手需要支持读取 `SKILL.md`；也可直接指定安装后的入口路径。已有同名版本时先比较并备份，宿主可能需要刷新会话。

DOCX 实际格式验收需要 WPS 及相应操作工具。仅检查 DOCX 时，无须导出 PDF、安装 PDF 检查依赖或比较 XML。字体按合法授权自行准备，本仓库不附带或自动安装字体，也不自动控制 WPS。

<a id="resources"></a>
## 文档与工具

| 文档 | 内容 |
| :--- | :--- |
| [Skill 入口](skills/zju-thesis-format/SKILL.md) | 两种模式、执行方法和检查要求 |
| [内置排版方案](skills/zju-thesis-format/references/builtin-format.md) | 可直接采用的格式参数及覆盖边界 |
| [母版逐项复核](skills/zju-thesis-format/references/source-format-audit.md) | 实际设置、明确标注、差异采用和未实测项 |
| [内置继承与覆盖](skills/zju-thesis-format/references/builtin-inheritance.md) | 默认值、样式、编号及直接设置；逐项标注验证范围 |
| [自定义模板参数提取](skills/zju-thesis-format/references/wps-profile.md) | 从其他 DOCX 模板建立配置 |
| [DOCX 格式验收](skills/zju-thesis-format/references/full-manuscript-validation.md) | WPS 实际格式、保存重开及按需 PDF 检查 |
| [参考文献缩进实测](skills/zju-thesis-format/references/bibliography-indent-validation.md) | 保留组合设置的有限 WPS 往返结果 |
| [自动目录实测](skills/zju-thesis-format/references/automatic-toc-validation.md) | 标题层级、长标题换行、多页目录、更新后修正及跳转 |
| [前置编号与正文重启](skills/zju-thesis-format/references/front-numbering-validation.md) | 无编号前页、前置连续编号、正文重启及目录对应；字体保留项另记 |
| [论文封面复用](skills/zju-thesis-format/references/thesis-cover-validation.md) | 母版校名、校徽、字段与题目填写设置及有限 WPS 结果 |
| [长题注、图文与跨页表格](skills/zju-thesis-format/references/figure-table-layout-validation.md) | 多行题注、嵌入式图片顺序、跨页续行及保留范围 |
| [重复表头与续表题](skills/zju-thesis-format/references/table-continuation-validation.md) | 多行/合并表头重复、显式续题、内容变化与自动候选限制 |
| [浮动图片与页末图题](skills/zju-thesis-format/references/floating-caption-validation.md) | 原锚点与环绕复用、实际分离后的局部绑定及重开结果 |
| [校徽图片复用](skills/zju-thesis-format/references/cover-emblem-validation.md) | 来源首页对象的尺寸、位置、排布与图像质量边界 |
| [字体排查](skills/zju-thesis-format/references/pdf-font-output.md) | 缺字体提示、实际调用、嵌入及检索 |
| [章标题与页眉页码](skills/zju-thesis-format/references/chapter-layout-validation.md) | 对象设置、静态章名分节实测与自动更新边界 |
| [有限实测记录](skills/zju-thesis-format/references/font-validation-2026-10-23.md) | 实测环境、结果与覆盖范围 |

> [!NOTE]
> 内置参数来自源 DOCX 实际设置及明确标注；差异和采用方式见[复核表](skills/zju-thesis-format/references/source-format-audit.md)。本轮所查行距、标题加粗、题注和表线已有[独立样稿有限实测](skills/zju-thesis-format/references/annotation-format-validation.md)；来源核查与 WPS 实测分别记录。已验证修正方法与尚未验证范围[分别列出](skills/zju-thesis-format/SKILL.md#尚未验证的范围)。中文长标题自然换行、多页目录、末行页码对齐和按需整条同页已有有限 DOCX 样稿通过记录；无编号封面/声明衔接前置大写罗马连续编号与正文单次重启，也已有独立样稿证据，属于按确认方案采用的技术适配。新增前页仍有缺字体及云字体提示，具体触发项和实际映射尚未确认。超出该范围的标题、复杂前置编号、特殊公式及其他环境等，按实际对象另查，不预判为错误，也不以历史失败否定已修正通过的结果。

<details>
<summary><strong>可选：PDF 辅助检查</strong></summary>

需要 Python 3.9+。在仓库根目录安装依赖并运行：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python skills/zju-thesis-format/scripts/check_pdf_text.py /path/to/output.pdf
```

Windows 使用 `.venv\Scripts\python.exe`。单独复制 skill 后，使用其 `requirements.txt` 和 `scripts/check_pdf_text.py`。

| 参数 | 用途 |
| :--- | :--- |
| `--font EXPECTED_POSTSCRIPT_NAME` | 检查指定字体；默认不指定 |
| `--docx /path/to/saved.docx` | 辅助检查正文段落是否包含在 PDF 提取结果中 |
| `--include-missing-text` / `--include-source-path` | 显式输出诊断原文或路径，分享前须检查 |

脚本默认隐藏原文与源文件路径，无遥测或自动上传。它检查文字提取及字体资源中的嵌入流、映射是否存在，不能代替实际字体、阅读器检索或视觉检查。

开发测试：`.venv/bin/python -m unittest discover -s tests -v`。现有 13 项合成检查包括 9 项 PDF/XML 辅助检查和 4 项目录恢复检查，不代表 WPS 渲染测试。检查范围见[审计记录](docs/sync-audit-2026-10-23.md)。

</details>

<a id="sources"></a>
## 来源与许可

内置方案的格式参考为**浙江大学工程师学院研究生论文 DOCX 格式母版**。自定义模式以使用者选择的模板及适用要求为依据；[zjuthesis 固定版本](skills/zju-thesis-format/references/zjuthesis-comparison.md)仅作实现参考。

本项目是社区工具，非浙江大学或 WPS 官方模板。参考母版的官方发布身份、版次和现行适用性未独立核实，使用前请核对本专业、学位类型及提交要求。详见[来源说明](skills/zju-thesis-format/references/format-rules.md)。

原创文档和脚本采用 **[MIT 许可证](LICENSE)**，必要的上游署名见[第三方声明](THIRD_PARTY_NOTICES.md)。仓库不包含论文、原始母版、私有日志、截图或字体文件。
