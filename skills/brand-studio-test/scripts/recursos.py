"""Verifica que los recursos binarios empaquetados (fuente, plantilla, logo)
llegan intactos al entorno y que se pueden usar para generar archivos.

Uso: python scripts/recursos.py [--salida CARPETA]
"""
import argparse
import hashlib
import json
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
CARPETAS_SALIDA = ["/mnt/user-data/outputs", "/mnt/data"]


def escribible(d: Path) -> bool:
    try:
        d.mkdir(parents=True, exist_ok=True)
        prueba = d / ".brand_studio_test"
        prueba.write_text("ok")
        prueba.unlink()
        return True
    except OSError:
        return False


def carpeta_salida(arg):
    """--salida si se indica; si no, la carpeta de descargas de la plataforma;
    si no, el directorio actual (si no es la carpeta de la Skill); si no, /tmp."""
    if arg:
        return Path(arg)
    for d in CARPETAS_SALIDA:
        if Path(d).is_dir() and escribible(Path(d)):
            return Path(d)
    cwd = Path.cwd()
    if SKILL_DIR not in (cwd, *cwd.parents) and escribible(cwd):
        return cwd
    return Path("/tmp/brand-studio-output")


def verificar():
    print("--- Integridad de recursos empaquetados ---")
    manifest = SKILL_DIR / "assets" / "manifest.json"
    if not manifest.exists():
        print(f"[FALTA] {manifest} (no llegaron los recursos)")
        return False
    todo_ok = True
    for rel, esperado in json.loads(manifest.read_text()).items():
        p = SKILL_DIR / rel
        if not p.exists():
            print(f"[FALTA] {rel}")
            todo_ok = False
            continue
        real = hashlib.sha256(p.read_bytes()).hexdigest()
        if real == esperado:
            print(f"[OK]    {rel} ({p.stat().st_size} bytes, sha256 coincide)")
        else:
            print(f"[DAÑADO] {rel} (sha256 no coincide: el archivo llegó modificado)")
            todo_ok = False
    return todo_ok


def generar_pptx(salida: Path):
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.util import Inches, Pt

    prs = Presentation(str(SKILL_DIR / "assets" / "plantilla_prueba.pptx"))
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.shapes.add_picture(str(SKILL_DIR / "assets" / "logo_prueba.png"), Inches(0.6), Inches(0.5), height=Inches(1))
    box = slide.shapes.add_textbox(Inches(1), Inches(3), Inches(11.3), Inches(1.5))
    run = box.text_frame.paragraphs[0].add_run()
    run.text = "Plantilla, logo y fuente empaquetados"
    run.font.name = "Bitstream Vera Sans"
    run.font.size = Pt(40)
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    destino = salida / "brand_studio_recursos.pptx"
    prs.save(str(destino))
    print(f"[OK]    PPTX con plantilla y logo: {destino}")


def generar_png(salida: Path):
    from PIL import Image, ImageDraw, ImageFont

    fuente = ImageFont.truetype(str(SKILL_DIR / "fonts" / "Vera.ttf"), 72)
    print(f"[OK]    Pillow cargó la fuente empaquetada: {' '.join(fuente.getname())}")
    img = Image.new("RGB", (1080, 1080), (30, 27, 75))
    logo = Image.open(SKILL_DIR / "assets" / "logo_prueba.png")
    img.paste(logo, ((1080 - logo.width) // 2, 200), logo)
    ImageDraw.Draw(img).text((540, 640), "Fuente Vera", font=fuente, fill="white", anchor="mm")
    destino = salida / "brand_studio_recursos.png"
    img.save(destino)
    print(f"[OK]    PNG 1080x1080 con logo y fuente: {destino}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida")
    salida = carpeta_salida(ap.parse_args().salida)
    salida.mkdir(parents=True, exist_ok=True)
    print("=== Brand Studio - prueba de recursos ===")
    print(f"Carpeta de la Skill: {SKILL_DIR}")
    print(f"Carpeta de salida:   {salida}")
    if verificar():
        print()
        print("--- Generacion con recursos ---")
        generar_pptx(salida)
        generar_png(salida)
    print("=== Fin de la prueba de recursos ===")


if __name__ == "__main__":
    main()
