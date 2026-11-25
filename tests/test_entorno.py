"""Pruebas de humo: las librerías del stack se importan y generan archivos."""
import pytest


def test_pptx(tmp_path):
    from pptx import Presentation
    prs = Presentation()
    prs.slides.add_slide(prs.slide_layouts[0]).shapes.title.text = "Brand Studio"
    out = tmp_path / "a.pptx"
    prs.save(out)
    assert out.stat().st_size > 0


def test_docx(tmp_path):
    from docx import Document
    doc = Document()
    doc.add_heading("Brand Studio", 0)
    out = tmp_path / "a.docx"
    doc.save(out)
    assert out.stat().st_size > 0


def test_pdf(tmp_path):
    from reportlab.pdfgen import canvas
    out = tmp_path / "a.pdf"
    c = canvas.Canvas(str(out))
    c.drawString(72, 720, "Brand Studio")
    c.save()
    assert out.stat().st_size > 0


def test_pillow(tmp_path):
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (1080, 1080), "white")
    ImageDraw.Draw(img).text((40, 40), "Brand Studio", fill="black")
    out = tmp_path / "a.png"
    img.save(out)
    assert out.stat().st_size > 0


def test_jinja_y_jsonschema():
    from jinja2 import Template
    import jsonschema
    assert Template("Hola {{ marca }}").render(marca="Riwi") == "Hola Riwi"
    jsonschema.validate({"marca": "Riwi"}, {"type": "object", "required": ["marca"]})


def test_cairosvg(tmp_path):
    try:
        import cairosvg
    except OSError as e:  # falta la librería nativa cairo (común en Windows)
        pytest.skip(f"cairo nativo no disponible: {e}")
    out = tmp_path / "a.png"
    cairosvg.svg2png(bytestring=b'<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"/>', write_to=str(out))
    assert out.stat().st_size > 0
