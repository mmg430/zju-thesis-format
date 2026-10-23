# 可选 PDF 工具与开发检查

仅在需要 PDF 输出时使用；这些检查不是 DOCX 在 WPS 中验收的前提。以下命令在仓库根目录运行。

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

开发测试：`.venv/bin/python -m unittest discover -s tests -v`。现有 13 项合成检查包括 9 项 PDF/XML 辅助检查和 4 项目录恢复检查，不代表 WPS 渲染测试。检查范围见[审计记录](sync-audit-2026-10-23.md)。
