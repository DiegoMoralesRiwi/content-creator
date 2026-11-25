"""Empaqueta cada Skill de skills/ en dos formatos:

  dist/claude/<skill>.zip   -> <skill>/SKILL.md ...            (subir como Skill en Claude)
  dist/chatgpt/<skill>.zip  -> plugin.json, .codex-plugin/plugin.json,
                               skills/<skill>/SKILL.md ...     (subir como complemento en ChatGPT)

Los metadatos del complemento de ChatGPT salen de skills/<skill>/chatgpt.json
(displayName, shortDescription, description, defaultPrompt, category) y de
tools/build_config.json (autor). La versión sale del archivo VERSION.

Uso: py tools/build_skills.py [nombre-skill ...]
"""
import json
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
IGNORAR = {".gitkeep", "__pycache__", ".DS_Store", "chatgpt.json"}


def archivos(skill_dir: Path):
    for f in sorted(skill_dir.rglob("*")):
        if f.is_file() and not IGNORAR.intersection(f.relative_to(skill_dir).parts):
            yield f


def manifiestos_chatgpt(nombre: str, meta: dict, autor: dict, version: str):
    descripcion = meta["description"]
    codex = {
        "author": autor,
        "description": descripcion,
        "interface": {
            "capabilities": [],
            "category": meta.get("category", "Other"),
            "defaultPrompt": meta["defaultPrompt"],
            "developerName": autor["name"],
            "displayName": meta["displayName"],
            "longDescription": meta.get("longDescription", descripcion),
            "shortDescription": meta["shortDescription"],
        },
        "keywords": meta.get("keywords", []),
        "name": nombre,
        "skills": "./skills",
        "version": version,
    }
    plugin = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "author": autor,
        "description": descripcion,
        "extensions": {
            "com.openai": {
                "interface": {
                    "defaultPrompt": meta["defaultPrompt"],
                    "developerName": autor["name"],
                    "displayName": meta["displayName"],
                    "shortDescription": meta["shortDescription"],
                }
            }
        },
        "name": nombre,
        "version": version,
    }
    return codex, plugin


def empaquetar(skill_dir: Path) -> list[Path]:
    nombre = skill_dir.name
    if not (skill_dir / "SKILL.md").exists():
        raise SystemExit(f"{nombre}: falta SKILL.md")
    meta_path = skill_dir / "chatgpt.json"
    if not meta_path.exists():
        raise SystemExit(f"{nombre}: falta chatgpt.json (metadatos del complemento de ChatGPT)")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    autor = json.loads((RAIZ / "tools" / "build_config.json").read_text(encoding="utf-8"))["author"]
    version = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()

    salidas = []
    # Claude
    claude = RAIZ / "dist" / "claude" / f"{nombre}.zip"
    claude.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(claude, "w", zipfile.ZIP_DEFLATED) as z:
        for f in archivos(skill_dir):
            z.write(f, Path(nombre) / f.relative_to(skill_dir))
    salidas.append(claude)

    # ChatGPT
    chatgpt = RAIZ / "dist" / "chatgpt" / f"{nombre}.zip"
    chatgpt.parent.mkdir(parents=True, exist_ok=True)
    codex, plugin = manifiestos_chatgpt(nombre, meta, autor, version)
    with zipfile.ZipFile(chatgpt, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(".codex-plugin/plugin.json", json.dumps(codex, indent=2, ensure_ascii=False))
        z.writestr("plugin.json", json.dumps(plugin, indent=2, ensure_ascii=False) + "\n")
        for f in archivos(skill_dir):
            z.write(f, Path("skills") / nombre / f.relative_to(skill_dir))
    salidas.append(chatgpt)

    for s in salidas:
        print(f"{s.relative_to(RAIZ)}  ({s.stat().st_size / 1024:.1f} KB)")
    return salidas


if __name__ == "__main__":
    nombres = sys.argv[1:] or sorted(
        p.name for p in (RAIZ / "skills").iterdir() if (p / "chatgpt.json").exists()
    )
    for n in nombres:
        empaquetar(RAIZ / "skills" / n)
