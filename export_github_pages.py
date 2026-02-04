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

ROUTE_TO_FILE = {
    "/": "index.html",
    "/solar-shades": "solar_shades.html",
    "/murals": "murals.html",
    "/urban-farming": "urban_farming.html",
    "/unreal-viewer": "unreal_viewer.html",
    "/compare": "compare.html",
    "/visualization-studio": "visualization_studio.html",
    "/before-after": "before_after.html",
    "/design-workspace": "design_workspace.html",
    "/scenarios": "scenarios.html",
    "/plant-library": "plant_library.html",
    "/live-dashboard": "live_dashboard.html",
    "/innovation-alleys-map": "innovation_alleys_map.html",
    "/existing": "existing.html",
}


def _rewrite_internal_routes(content: str) -> str:
    # Rewrite known Flask route href/src targets to static HTML files.
    for route, filename in ROUTE_TO_FILE.items():
        content = content.replace(f'href="{route}"', f'href="{filename}"')
        content = content.replace(f"href='{route}'", f"href='{filename}'")
        content = content.replace(f"window.location='{route}'", f"window.location='{filename}'")
        content = content.replace(f'window.location="{route}"', f'window.location="{filename}"')
        content = content.replace(f"location.href='{route}'", f"location.href='{filename}'")
        content = content.replace(f'location.href="{route}"', f'location.href="{filename}"')

    # Convert any remaining root-absolute same-site links to relative.
    # This avoids breaking under https://<user>.github.io/<repo>/
    content = re.sub(r'href="/(?!/)([^"]+)"', r'href="\1"', content)
    content = re.sub(r"href='/(?!/)([^']+)'", r"href='\1'", content)
    return content


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

        content = _rewrite_internal_routes(content)

        out_path = DOCS_DIR / html_path.name
        out_path.write_text(content, encoding="utf-8")

    # GitHub Pages expects index.html
    src_home = DOCS_DIR / "index_unified.html"
    if src_home.exists():
        shutil.copyfile(src_home, DOCS_DIR / "index.html")


if __name__ == "__main__":
    export()
    print("GitHub Pages export complete: docs/")
