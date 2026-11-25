import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "skills" / "brand-studio-test"


def test_hola_pptx(tmp_path):
    out = tmp_path / "x.pptx"
    subprocess.run([sys.executable, SKILL / "scripts" / "hola_pptx.py", "--salida", out], check=True)
    from pptx import Presentation

    assert len(Presentation(out).slides) == 2


def test_diagnostico_corre():
    r = subprocess.run([sys.executable, SKILL / "scripts" / "diagnostico.py"],
                       capture_output=True, text=True, encoding="utf-8", check=True)
    assert "Fin del diagnostico" in r.stdout


def test_build_zip():
    subprocess.run([sys.executable, RAIZ / "tools" / "build_skills.py", "brand-studio-test"], check=True)
    with zipfile.ZipFile(RAIZ / "dist" / "brand-studio-test.zip") as z:
        assert "brand-studio-test/SKILL.md" in z.namelist()
