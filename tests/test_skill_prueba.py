import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "skills" / "brand-studio-test"


def correr(*args):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True,
                          encoding="utf-8", check=True,
                          env={**os.environ, "PYTHONIOENCODING": "utf-8"}).stdout


def test_hola_pptx(tmp_path):
    out = tmp_path / "x.pptx"
    correr(SKILL / "scripts" / "hola_pptx.py", "--salida", out)
    from pptx import Presentation

    assert len(Presentation(out).slides) == 2


def test_diagnostico_corre():
    assert "Fin del diagnostico" in correr(SKILL / "scripts" / "diagnostico.py")


def test_recursos(tmp_path):
    salida = correr(SKILL / "scripts" / "recursos.py", "--salida", tmp_path)
    assert "[FALTA]" not in salida and "[DAÑADO]" not in salida
    assert (tmp_path / "brand_studio_recursos.pptx").exists()
    assert (tmp_path / "brand_studio_recursos.png").exists()


def test_build_dos_formatos():
    correr(RAIZ / "tools" / "build_skills.py", "brand-studio-test")
    with zipfile.ZipFile(RAIZ / "dist" / "claude" / "brand-studio-test.zip") as z:
        nombres = z.namelist()
        assert "brand-studio-test/SKILL.md" in nombres
        assert "brand-studio-test/fonts/Vera.ttf" in nombres
        assert not any(n.endswith("chatgpt.json") for n in nombres)
    with zipfile.ZipFile(RAIZ / "dist" / "chatgpt" / "brand-studio-test.zip") as z:
        nombres = z.namelist()
        assert "plugin.json" in nombres and ".codex-plugin/plugin.json" in nombres
        assert "skills/brand-studio-test/SKILL.md" in nombres
        assert "skills/brand-studio-test/assets/plantilla_prueba.pptx" in nombres
        codex = json.loads(z.read(".codex-plugin/plugin.json"))
        assert codex["name"] == "brand-studio-test" and codex["skills"] == "./skills"
