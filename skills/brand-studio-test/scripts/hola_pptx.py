"""Genera una presentación PPTX mínima de prueba."""
import argparse

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt


def generar(salida):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    for titulo, texto in [
        ("Brand Studio", "Prueba técnica de generación de presentaciones"),
        ("Funciona", "Este archivo se generó dentro del entorno de la plataforma."),
    ]:
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        fondo = slide.background.fill
        fondo.solid()
        fondo.fore_color.rgb = RGBColor(0x11, 0x11, 0x11)
        for txt, top, size in [(titulo, 2.6, 54), (texto, 3.9, 24)]:
            box = slide.shapes.add_textbox(Inches(1), Inches(top), Inches(11.3), Inches(1.2))
            run = box.text_frame.paragraphs[0].add_run()
            run.text = txt
            run.font.size = Pt(size)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    prs.save(salida)
    print(f"Presentacion generada: {salida}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="brand_studio_prueba.pptx")
    generar(ap.parse_args().salida)
