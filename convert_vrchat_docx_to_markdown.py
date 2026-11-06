from pathlib import Path
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(r"D:\dev\01memo")
SRC = ROOT / "VRChat_自作小物をアバターに取り入れる手順_Note記事原稿.docx"
OUT = ROOT / "VRChat_自作小物をアバターに取り入れる手順_Note記事原稿.md"


def blocks(doc):
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag.endswith("}p"):
            yield Paragraph(child, doc)
        elif child.tag.endswith("}tbl"):
            yield Table(child, doc)


def clean(text):
    return text.replace("\u00a0", " ").strip()


doc = Document(SRC)
out = []
seen_title = False

for block in blocks(doc):
    if isinstance(block, Paragraph):
        text = clean(block.text)
        if not text:
            continue
        style = block.style.name if block.style else ""

        if text == "BEGINNER'S CREATION GUIDE":
            continue
        if text.startswith("VRChatで自作の小物を") and not seen_title:
            out += ["# VRChatで自作の小物をアバターに取り入れる手順", ""]
            seen_title = True
            continue
        if text.startswith("Blenderなどで作ったアクセサリーをUnityへ"):
            out += [f"*{text.replace(chr(10), ' ')}*", ""]
            continue
        if text.startswith("想定読者：") or text.startswith("所要時間の目安："):
            out += [f"**{text}**", ""]
            continue
        if style == "Heading 1":
            out += [f"## {text}", ""]
        elif style == "Heading 2":
            out += [f"### {text}", ""]
        elif style == "Heading 3":
            out += [f"#### {text}", ""]
        elif style.startswith("List Bullet"):
            lines = text.splitlines()
            out.append(f"- {lines[0]}")
            for line in lines[1:]:
                out.append(f"  {line}")
        elif text.startswith("STEP "):
            # Noteで見つけやすい小見出しにする。
            parts = text.split("  ", 1)
            out += [f"### {parts[-1]}", ""]
        elif text.startswith("□  "):
            out.append(f"- [ ] {text[3:]}")
        elif len(text) > 2 and text[0].isdigit() and text[1] == ".":
            out.append(text)
        elif text.startswith("#VRChat"):
            out += [text, ""]
        elif text.startswith("※"):
            out += [f"> {text}", ""]
        else:
            # Word内の強調段落をMarkdownでも保持。
            bold_only = bool(block.runs) and all(r.bold for r in block.runs if r.text.strip())
            out += [f"**{text}**" if bold_only else text, ""]

    else:
        rows = [[clean(c.text) for c in row.cells] for row in block.rows]
        if not rows:
            continue
        if len(rows[0]) == 1:
            lines = rows[0][0].splitlines()
            if lines and lines[0].startswith("IMAGE  |"):
                caption = " ".join(lines[1:]) if len(lines) > 1 else "スクリーンショット"
                out += [f"> **画像挿入：** {caption}", ""]
            else:
                label = lines[0] if lines else "ポイント"
                body = " ".join(lines[1:])
                out += [f"> **{label}**", f"> {body}" if body else ">", ""]
        elif len(rows[0]) == 2 and len(rows) > 1:
            out += [f"| {rows[0][0]} | {rows[0][1]} |", "|---|---|"]
            for a, b in rows[1:]:
                out.append(f"| {a.replace('|', '｜')} | {b.replace('|', '｜')} |")
            out.append("")

# 余分な空行を1行へ圧縮。
final = []
for line in out:
    structural = line.startswith(("#", ">", "|"))
    if structural and final and final[-1] != "" and not final[-1].startswith((">", "|")):
        final.append("")
    if line == "" and final and final[-1] == "":
        continue
    final.append(line)

OUT.write_text("\n".join(final).strip() + "\n", encoding="utf-8")
print(OUT)
