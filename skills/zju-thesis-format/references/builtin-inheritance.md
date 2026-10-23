# 内置方案的继承与覆盖

本页补充[参数表](builtin-format.md)的属性来源。以下已回查参考 DOCX 的 XML；**除[参考文献组合缩进专项](bibliography-indent-validation.md)外，新增信息未经 WPS 保存重开与导出实测**；字体等范围仍见[既有实测](font-validation-2026-10-23.md)。只公开格式属性，不包含示例文字或源文件。

## 读取和应用方式

- 分开记录文档默认值、表格/编号属性、段落样式及 `basedOn`、字符样式及 `basedOn`、段落直接属性、文字 run 直接属性。`link` 是关联字符样式，不是额外的 `basedOn` 父级。
- `pPr/rPr` 是段落标记的字符属性，不能据此覆盖所有文字。读取标题时也不要把嵌套文本框中的说明文字算成标题 run。
- 字体按 `ascii / hAnsi / eastAsia / cs` 及对应主题分别处理。`sz / szCs` 单位为半磅；`b / bCs` 分开保留；缺省、显式关闭和开启不能混为一项。不要用字典简单覆盖来计算样式开关属性。
- 下列样式 ID 仅用于解释源结构；迁移时按对象建立映射，不能假定目标文档同 ID 即同样式。无独立段落样式的对象也不要擅自套用现成的 Heading 或 TOC 样式。
- 这是补充属性清单，不是完整样式库。没有列出的属性仍按参数表保留目标已有设置并记录缺口；要求逐属性复制时使用自定义模板模式。

## 默认值与标题正文

| 层次 / 对象 | 已读取属性及关系 | 应用边界 |
| --- | --- | --- |
| 文档字符默认值 | `asciiTheme=minorHAnsi`、`hAnsiTheme=minorHAnsi`、`eastAsiaTheme=minorEastAsia`、`cstheme=minorBidi`；`sz=21`、`szCs=22`、`kern=2`；语言 en-US / zh-CN / ar-SA；段落默认属性为空 | 不能把默认 10.5 磅套给全部正文 |
| Normal（源 ID `a`） | 无 basedOn；`jc=both`、`widowControl=0`；`sz=24`、`szCs=24`，未单列 rFonts | 常用正文 12 磅来自这一层；字体仍需看直接设置与主题 |
| 章标题样式（`1`） | basedOn Normal，link `10`；keepNext、keepLines、snapToGrid=0、before=440、after=240、居中、outlineLvl=0；西文/复杂文种 Times New Roman，东亚黑体；sz=32、szCs=44、bCs 开启、kern=44 | **可见章标题 run 另设东亚仿宋、b 开启、sz=30、szCs=30**。不能只复制样式而丢失直接覆盖，也不能把底层黑体当成最终章标题字体 |
| 一级节标题样式（`2`） | basedOn Normal，link `20`；keepNext、keepLines、before/after=260、line=416 auto、outlineLvl=1；西文 Cambria、东亚宋体、cs=Times New Roman；b/bCs 开启、sz/szCs=32 | 对应标题 run 直接设西文 Times New Roman、东亚仿宋、sz/szCs=28、bCs=0；普通文字加粗来自样式。底层 Cambria 仍是诊断对象 |
| 关联字符样式（`10`、`20`） | basedOn Default Paragraph Font（`a0`），分别 link 回章/节样式；各自保留与对应标题样式相同的字体、字号等字符声明；`a0` 无自列字符属性 | 未实际引用时也不能无依据认定与字体提示无关；不能把 link 当作所有 run 的自动字符样式 |
| 二级节标题 | 无显式 pStyle，使用 Normal；段落直接 line=360 auto、widowControl 开启、autoSpaceDE/DN=0；文字直接设仿宋 / Times New Roman、kern=0，未直接设 sz | 普通字号继承 Normal 的 12 磅；不是 Heading 3，不补造大纲级别或段距 |
| 普通正文 | 无显式 pStyle，使用 Normal；直接 line=360 auto、firstLine=480、adjustRightInd=0、snapToGrid=0；run 直接设仿宋 / Times New Roman，部分 szCs=22 | 普通字号与复杂文种字号分开处理，不强行统一 |
| 致谢、中文摘要、附录正文 | 对应所查段落无显式 pStyle；line=480 exact，firstLineChars=200 与 firstLine=480 并存 | 中文摘要有局部 run 明确 sz/szCs=28，其余普通文字可继承 12 磅；不能按段落标记的 14 磅统一整段 |
| Abstract 标题 | 无显式 pStyle；居中、snapToGrid=0、beforeLines=100 与 before=312 并存；run 西文/复杂文种 Times New Roman、东亚声明方正小标宋简体，sz/szCs=30 | 英文显示 TNR 不等于东亚声明可删除；段前两个单位字段不相加换算 |
| Abstract 正文 | 无显式 pStyle；line=480 exact、firstLineChars=200 与 firstLine=480；直接字体西文 Times New Roman、东亚仿宋 | 普通字号继承 Normal；保持脚本差异 |

## 目录、题注、表格与书目

| 对象 | 已读取的层次 | 应用边界 |
| --- | --- | --- |
| 目录标题 / 图表目录标题 | 目录标题无显式 pStyle，直接居中、仿宋/TNR、b、sz/szCs=30；图表目录标题引用章标题样式并有仿宋 15 磅直接覆盖 | 不把目录标题套成有章标题段距的样式 |
| 目录条目 | 所查条目无显式 pStyle；直接 line=360 auto；右制表位 pos=6141 twip、leader=dot；run 有常规、加粗及局部 sz/szCs=28 等差异 | 未取得可复用的 TOC 层级样式链；所查域指令不含 TOC。不可补造各级缩进、统一条目字号，或声称源文件已设置自动目录；自动目录配置须另行适配并重验 |
| 图题 / 表题 | 无显式 pStyle，字号由 run 直接 sz/szCs=21；居中；表题直接 firstLine=482；中英文 run 字体按参数表区分 | 不因缺少命名 Caption 样式而推断单倍行距；未列行距保留继承 |
| 表格样式 | 所查表引用 TableGrid（`aa`），basedOn 默认表样式（`a1`）；默认单元格上下边距 0、左右 108 twip，表缩进 0；TableGrid 自列 Calibri/宋体/TNR、sz/szCs=20，六方向边框 single、sz=4 | 单元格文字的仿宋/TNR 10.5 磅直接设置覆盖底层；不能把底层 Calibri 当成表内最终字体 |
| 表格直接属性 | 所查表直接取消左、右、内部横竖线；部分单元格另设 top/bottom single、sz=4；表宽 auto，表缩进 1384 twip | 边框同时受表级和单元格设置影响。缩进是所查对象的几何属性，不推广为所有表格的统一位置；列宽、合并、续表另查，不从示例行列数生成目标表 |
| 参考文献条目样式 | ListParagraph1 basedOn Normal；line=360 auto、adjustRightInd=0、snapToGrid=0；firstLineChars=200、firstLine=420；仿宋/TNR，szCs=22 | 普通字号继承 12 磅；不要仅复制样式而丢失编号定义 |
| 参考文献编号 | 条目引用 numId=1、ilvl=0，关联 abstractNumId=0；该级 decimal、start=1、lvlText=`[%1]`、lvlJc=left；编号级 ind left=420、hanging=420 twip，编号字形 TNR、sz/szCs=24 | 迁移时重映射编号 ID；start 是列表定义，不是固定页码。只记录所用级，不补造其余级 |
| 参考文献直接属性 | 条目 jc=left、widowControl 开启、firstLineChars=0；run 有 szCs=21、kern=0 的局部设置 | 样式首行、编号悬挂和直接字符缩进须一起保留；组合保持原样后已在指定 WPS 的单/双位数编号样稿中通过往返；首行文字与续行实测均距正文左边界 21 磅。仍不能将 hanging=420 单独当作可替代整组属性的规则，见专项记录 |

## 页眉页脚及主题

| 对象 | 已读取属性 | 应用边界 |
| --- | --- | --- |
| 页眉样式（`a8`） | basedOn Normal，link `a9`；sz/szCs=18；居中、snapToGrid=0；制表位 center=4153 / right=8306 twip；底边 single、sz=6（0.75 磅）、space=1、color=auto | 所查页眉有宋体直接声明，也有直接段落对齐差异；不能把样式居中视为所有节的最终对齐 |
| 页脚样式（`a3`） | basedOn Normal，link `a4`；sz/szCs=18；左对齐、snapToGrid=0；制表位同页眉 | 页码所在段落另有 framePr：wrap=around、vAnchor=text、hAnchor=margin、xAlign=center、y=1。框架居中不等于段落 jc=center |
| 字符样式及域 | 页眉/页脚关联字符样式 basedOn `a0`、sz/szCs=18；页码字符样式 `a5` basedOn `a0`，无自列字符属性；页码为 PAGE 域 | 页码字体尚须结合默认值和实际输出核对；不复制示例页码起点、节序或页眉章名，不声称自动跨章映射已验证 |
| 主题字体 | major Latin=Calibri Light，minor Latin=Calibri；Hans 均宋体，Hant 均新細明體；Jpan major=ＭＳ ゴシック、minor=ＭＳ 明朝；ea/cs 基础 typeface 为空 | 脚本映射声明不是实际调用证据；空 typeface 也不等于没有可继承字体。按[字体诊断](pdf-font-output.md)定位，不能据映射表要求全部安装 |

记录格式时保留这些层次；没有实际渲染证据时只报告“属性已核对”。涉及分页、目录定位、编号对齐、字体映射或页眉定位的结果，在目标环境完成相应检查后才能标为通过。
