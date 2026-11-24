"""Builds styled-by-people-mockup.html from mockup-src.html.

Every 'IMG:<filename>' in the source is replaced with that file from
mockup-images/, embedded as a data URI, so the mockup opens anywhere.
Run:  python build-mockup.py
"""
import base64
import pathlib
import re

HERE = pathlib.Path(__file__).parent
MIME = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}


def embed(match):
    name = match.group(1)
    path = HERE / "mockup-images" / name
    ext = name.rsplit(".", 1)[-1].lower()
    data = base64.b64encode(path.read_bytes()).decode()
    return f"data:image/{MIME[ext]};base64,{data}"


src = (HERE / "mockup-src.html").read_text(encoding="utf-8")
out = re.sub(r"IMG:([^'\"]+)", embed, src)
(HERE / "styled-by-people-mockup.html").write_text(out, encoding="utf-8")
print(f"Built styled-by-people-mockup.html ({len(out) // 1024} KB)")
