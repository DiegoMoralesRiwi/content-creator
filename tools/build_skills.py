"""Empaqueta cada carpeta de skills/ en dist/<skill>.zip.

Uso: py tools/build_skills.py [nombre-skill ...]
"""
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
IGNORAR = {".gitkeep", "__pycache__", ".DS_Store"}


def empaquetar(skill_dir: Path) -> Path:
    if not (skill_dir / "SKILL.md").exists():
        raise SystemExit(f"{skill_dir.name}: falta SKILL.md")
    dist = RAIZ / "dist"
    dist.mkdir(exist_ok=True)
    destino = dist / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file() and not IGNORAR.intersection(f.parts):
                z.write(f, Path(skill_dir.name) / f.relative_to(skill_dir))
    print(f"{destino.relative_to(RAIZ)}  ({destino.stat().st_size / 1024:.1f} KB)")
    return destino


if __name__ == "__main__":
    nombres = sys.argv[1:] or [p.name for p in (RAIZ / "skills").iterdir() if p.is_dir()]
    for n in nombres:
        empaquetar(RAIZ / "skills" / n)
