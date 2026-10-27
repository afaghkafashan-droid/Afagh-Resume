"""
سایت رزومه را می‌سازد.

اجرا:  python build.py
خروجی: output/index.html
"""

from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from resume_data import resume

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output"


def build() -> Path:
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("index.html")

    html = template.render(resume=resume, year=datetime.now().year)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_file = OUTPUT_DIR / "index.html"
    out_file.write_text(html, encoding="utf-8")
    return out_file


if __name__ == "__main__":
    path = build()
    print(f"✅ Built: {path}")
