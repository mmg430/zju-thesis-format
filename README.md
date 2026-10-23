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

你可以直接使用仓库中已有的排版参数，也可以提供自己的 DOCX 模板，通过同一套方法提取格式、建立新的排版配置。支持页面、标题、正文、图表、目录和参考文献的格式处理，以及 WPS 保存重开与 PDF 输出检查。

<a id="usage"></a>
## 两种用法

| 用法 | 需要准备 | 格式依据 |
| :--- | :--- | :--- |
| **直接使用内置方案** | 需要排版的文档 | 仓库已包含的[排版参数](skills/zju-thesis-format/references/builtin-format.md)，无需另行提供源母版 |
| **使用自定义模板** | 自己的 DOCX 模板和目标文档 | 提取模板对应对象的实际设置，建立新配置，不叠加内置参数 |

仅检查现有文档时保持只读，不自动应用任何方案；排版修改按明确选定的格式执行。

### 直接使用内置方案

```text
使用 $zju-thesis-format，按内置排版方案处理文档。
目标文档：<DOCX 路径>
在副本上应用已记录的页面、标题、正文、图表及书目参数。
未记录项保留原设置并说明；完成后核验 WPS 与 PDF 输出。
```

内置参数可直接查阅，包括页边距、字体、字号、行距和段距等。它是可复用的格式配置，不包含完整 DOCX 母版；样式、编号和直接格式的已知关系见[继承说明](skills/zju-thesis-format/references/builtin-inheritance.md)，未列属性保留并标明。

### 使用自定义模板

```text
使用 $zju-thesis-format，以我提供的模板建立排版配置。
模板：<模板 DOCX 路径>
目标文档：<目标 DOCX 路径>
逐对象提取实际设置，保留字体、样式继承和段内差异。
不套用内置参数；在副本上完成排版，并核验 WPS 与 PDF 输出。
```

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

实际保存重开和导出检查需要 WPS 及相应操作工具。字体按合法授权自行准备，本仓库不附带或自动安装字体，也不自动控制 WPS。

<a id="resources"></a>
## 文档与工具

| 文档 | 内容 |
| :--- | :--- |
| [Skill 入口](skills/zju-thesis-format/SKILL.md) | 两种模式、执行方法和检查要求 |
| [内置排版方案](skills/zju-thesis-format/references/builtin-format.md) | 可直接采用的格式参数及覆盖边界 |
| [内置继承与覆盖](skills/zju-thesis-format/references/builtin-inheritance.md) | 默认值、样式、编号及直接设置；新增属性未经 WPS 实测 |
| [自定义模板参数提取](skills/zju-thesis-format/references/wps-profile.md) | 从其他 DOCX 模板建立配置 |
| [WPS 与 PDF 检查](skills/zju-thesis-format/references/full-manuscript-validation.md) | 保存、关闭重开、导出和输出核验 |
| [字体排查](skills/zju-thesis-format/references/pdf-font-output.md) | 缺字体提示、实际调用、嵌入及检索 |
| [章标题与页眉页码](skills/zju-thesis-format/references/chapter-layout-validation.md) | 对象设置、分节及页眉页脚检查 |
| [有限实测记录](skills/zju-thesis-format/references/font-validation-2026-10-23.md) | 实测环境、结果与覆盖范围 |

> [!NOTE]
> 内置参数来自源 DOCX 实际属性；参数读取与 WPS 实测分别记录。现有实测结论仅适用于记录中的环境、样稿和检查项，其他文档或环境仍需核验实际输出。

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

开发测试：`.venv/bin/python -m unittest discover -s tests -v`。现有 9 项合成检查使用中性 PDF/XML，不代表 WPS 渲染测试。检查范围见[审计记录](docs/sync-audit-2026-10-23.md)。

</details>

<a id="sources"></a>
## 来源与许可

内置方案的格式参考为**浙江大学工程师学院研究生论文 DOCX 格式母版**。自定义模式以使用者选择的模板及适用要求为依据；[zjuthesis 固定版本](skills/zju-thesis-format/references/zjuthesis-comparison.md)仅作实现参考。

本项目是社区工具，非浙江大学或 WPS 官方模板。参考母版的官方发布身份、版次和现行适用性未独立核实，使用前请核对本专业、学位类型及提交要求。详见[来源说明](skills/zju-thesis-format/references/format-rules.md)。

原创文档和脚本采用 **[MIT 许可证](LICENSE)**，必要的上游署名见[第三方声明](THIRD_PARTY_NOTICES.md)。仓库不包含论文、原始母版、私有日志、截图或字体文件。
