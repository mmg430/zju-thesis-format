<div align="center">

# ZJU Thesis Format

**浙江大学研究生论文排版**

[内置格式](skills/zju-thesis-format/references/builtin-format.md) · [自定义模板](skills/zju-thesis-format/references/wps-profile.md) · [MIT License](LICENSE)

</div>

<a id="overview"></a>
面向浙江大学的研究生论文排版与核验工具。可直接采用内置格式，也可按自己的 DOCX 模板建立新配置。

<a id="usage"></a>
## 两种用法

| 模式 | 准备材料 | 格式依据 |
| :--- | :--- | :--- |
| **内置格式** | 目标 DOCX | 已包含的[参数与继承信息](skills/zju-thesis-format/references/builtin-inheritance.md)，无需另备源母版；未记录项保留并说明 |
| **自定义模板** | 模板及目标 DOCX | 提取模板实际设置与明确标注，不叠加内置参数 |

仅检查时保持只读；排版修改在副本中完成，保留原稿。

**采用内置格式**

```text
使用 $zju-thesis-format，按内置格式排版 <目标 DOCX 路径>。
在副本上处理，保留未记录属性；完成 WPS 保存关闭重开并检查实际格式。
```

**采用自己的模板**

```text
使用 $zju-thesis-format，以 <模板 DOCX 路径> 排版 <目标 DOCX 路径>。
复用对应对象的实际格式与明确标注，不叠加内置参数；在副本上完成 WPS 保存关闭重开检查。
```

## 格式、方法与限制

| 类别 | 内容 |
| :--- | :--- |
| **内置格式** | 页面、标题、正文、图表、目录、参考文献等对应参数；[参数表](skills/zju-thesis-format/references/builtin-format.md)区分来源属性与采用设置 |
| **已验证方法** | 目录更新后恢复格式、静态页眉同步、图题绑定、重复表头、显式续题等已有有限实测；定向修正后满足所选格式即可通过 |
| **剩余限制** | 自动续表题所测条件候选未通过；部分前页字体映射及其他复杂对象、环境仍待核对。方法通过不等于任意新稿自动合格 |

处理步骤：**应用所选格式 → WPS 检查 → 修正实际偏差 → 保存关闭重开确认。** 详细过程与覆盖范围见[验证记录索引](skills/zju-thesis-format/references/validation-index.md)，不沿用样稿固定页数或分表行号。

<a id="install"></a>
## 安装

将完整 skill 目录复制到目标项目。以下命令适用于 macOS / Linux 或 Git Bash；其他环境可手动复制整个目录：

```sh
git clone https://github.com/mmg430/zju-thesis-format.git
cd zju-thesis-format
mkdir -p /path/to/your-project/.agents/skills
cp -R skills/zju-thesis-format /path/to/your-project/.agents/skills/
```

替换项目路径；已有同名版本时先备份。助手需支持读取 `SKILL.md`，宿主可能需要刷新会话。WPS 验收需要相应操作工具；字体按合法授权自行准备，本仓库不附带字体、不自动安装或控制 WPS。

<a id="resources"></a>
## 文档

| 入口 | 用途 |
| :--- | :--- |
| [SKILL.md](skills/zju-thesis-format/SKILL.md) | 模式选择、实施、修正与验收 |
| [参数表](skills/zju-thesis-format/references/builtin-format.md) · [继承说明](skills/zju-thesis-format/references/builtin-inheritance.md) · [来源复核](skills/zju-thesis-format/references/source-format-audit.md) | 内置格式的依据与覆盖边界 |
| [自定义模板](skills/zju-thesis-format/references/wps-profile.md) | 提取其他 DOCX 的对应设置 |
| [验证记录索引](skills/zju-thesis-format/references/validation-index.md) | 各专项实测、修正方法及剩余限制 |
| [可选 PDF 工具](docs/pdf-tools.md) | 按需输出检查及开发检查说明，非 DOCX 验收前提 |

<a id="sources"></a>
## 来源与许可

内置格式参考**浙江大学工程师学院研究生论文 DOCX 格式母版**；[zjuthesis 固定版本](skills/zju-thesis-format/references/zjuthesis-comparison.md)仅作实现参考。项目为社区工具，非学校或 WPS 官方模板；来源身份和适用边界见[来源说明](skills/zju-thesis-format/references/format-rules.md)，使用前核对相应提交要求。

原创文档与脚本采用 [MIT 许可证](LICENSE)，上游署名见[第三方声明](THIRD_PARTY_NOTICES.md)。
