import os
import re
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
APP_DIR = REPO_ROOT / "PUHC_Alley3_Production"
TEMPLATES_DIR = APP_DIR / "templates"
STATIC_DIR = APP_DIR / "static"
DOCS_DIR = REPO_ROOT / "docs"


URL_FOR_STATIC_RE = re.compile(r"\{\{\s*url_for\('static',\s*filename='([^']+)'\)\s*\}\}")


def export() -> None:
    if not APP_DIR.exists():
        raise SystemExit(f"Missing {APP_DIR}")

    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    # Copy static assets
    docs_static = DOCS_DIR / "static"
    if docs_static.exists():
        shutil.rmtree(docs_static)
    shutil.copytree(STATIC_DIR, docs_static)

    # Copy and rewrite templates
    for html_path in sorted(TEMPLATES_DIR.glob("*.html")):
        content = html_path.read_text(encoding="utf-8")

        content = URL_FOR_STATIC_RE.sub(r"static/\1", content)
        content = content.replace('"/static/', '"static/')
        content = content.replace("'/static/", "'static/")
        content = content.replace("(/static/", "(static/")

        out_path = DOCS_DIR / html_path.name
        out_path.write_text(content, encoding="utf-8")

    # GitHub Pages expects index.html
    src_home = DOCS_DIR / "index_unified.html"
    if src_home.exists():
        shutil.copyfile(src_home, DOCS_DIR / "index.html")


if __name__ == "__main__":
    export()
    print("GitHub Pages export complete: docs/")
