"""Diagnóstico del entorno de ejecución para Brand Studio."""
import importlib
import platform
import shutil
import socket
import sys
from importlib import metadata
from pathlib import Path

LIBRERIAS = [
    ("pptx", "python-pptx"),
    ("docx", "python-docx"),
    ("PIL", "Pillow"),
    ("reportlab", "ReportLab"),
    ("jinja2", "Jinja2"),
    ("jsonschema", "jsonschema"),
    ("cairosvg", "CairoSVG"),
]

SKILL_DIR = Path(__file__).resolve().parent.parent


def version(distribucion):
    try:
        return metadata.version(distribucion)
    except metadata.PackageNotFoundError:
        return "?"


def main():
    print("=== Brand Studio - diagnostico del entorno ===")
    print(f"Python:  {sys.version.split()[0]}")
    print(f"Sistema: {platform.platform()}")
    print(f"Carpeta de la Skill: {SKILL_DIR}")
    print()
    print("--- Librerias ---")
    for mod_name, nombre in LIBRERIAS:
        try:
            importlib.import_module(mod_name)
            print(f"[OK]    {nombre} {version(nombre)}")
        except Exception as e:  # noqa: BLE001
            print(f"[FALTA] {nombre}: {type(e).__name__}: {str(e).splitlines()[0][:120]}")
    print()
    print("--- Binarios del sistema ---")
    for b in ["soffice", "libreoffice", "fc-list", "convert", "rsvg-convert", "inkscape"]:
        print(f"{'[OK]' if shutil.which(b) else '[NO]'}    {b}")
    print()
    print("--- Tipografias ---")
    fuentes = [p for p in (SKILL_DIR / "fonts").glob("*") if p.suffix.lower() in {".ttf", ".otf"}]
    print(f"Fuentes empaquetadas en la Skill: {len(fuentes)}")
    try:
        from PIL import ImageFont

        for f in fuentes:
            ImageFont.truetype(str(f), 24)
            print(f"[OK]    Pillow carga {f.name}")
    except Exception as e:  # noqa: BLE001
        print(f"[ERROR] cargando fuentes: {e}")
    sistema = 0
    for d in ["/usr/share/fonts", "/usr/local/share/fonts"]:
        if Path(d).exists():
            sistema += sum(1 for p in Path(d).rglob("*") if p.suffix.lower() in {".ttf", ".otf"})
    print(f"Fuentes del sistema (Linux): {sistema}")
    print()
    print("--- Red ---")
    try:
        socket.create_connection(("pypi.org", 443), timeout=3).close()
        print("[SI]    Acceso a internet (pypi.org)")
    except OSError:
        print("[NO]    Sin acceso a internet")
    print()
    print("--- Escritura ---")
    for d in ["/mnt/user-data/outputs", "/mnt/data", str(Path.cwd())]:
        p = Path(d)
        if p.exists():
            try:
                t = p / ".brand_studio_test"
                t.write_text("ok")
                t.unlink()
                print(f"[OK]    {d}")
            except OSError:
                print(f"[NO]    {d} (sin permiso)")
    print("=== Fin del diagnostico ===")


if __name__ == "__main__":
    main()
