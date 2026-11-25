# CLAUDE.md — Brand Studio

## Qué es este proyecto

Brand Studio genera materiales corporativos para **Riwi**, **Blackbird LATAM** y **Blackbird USA** desde ChatGPT y Claude (online), distribuidos como **Agent Skills** instalables. Sin APIs pagas, sin servidores, sin bases de datos, sin Figma. Costo recurrente objetivo: USD $0/mes.

Plan completo y fuente de verdad: [docs/plan-de-trabajo.md](docs/plan-de-trabajo.md).

Dos ambientes / dos paquetes:

| Skill | Usuarios | Salidas |
|---|---|---|
| `presentation-studio` | Equipo comercial | Presentaciones, propuestas, cotizaciones, casos de éxito, one-pagers — PPTX, DOCX, PDF |
| `content-studio` | Mercadeo y comunicaciones | Posts, carruseles, historias, banners, copy — PNG, JPG, SVG |

Ambos paquetes contienen los recursos de las **tres** marcas, pero las identidades se mantienen estrictamente separadas (nunca mezclar colores, logos, tono o datos entre Riwi, Blackbird LATAM y Blackbird USA; tampoco entre las dos Blackbird).

## Estructura

```
brands/<marca>/        riwi, blackbird-latam, blackbird-usa: Identidad visual/verbal, logos, tipografías, colores, plantillas, imágenes
engines/presentations/ Motor Python para PPTX/DOCX/PDF
engines/content/       Motor Python para imágenes de redes
knowledge/             Info corporativa, servicios, reglas comerciales, tono de voz
skills/<skill>/SKILL.md Instrucciones de cada Skill
tests/                 pytest
build/, dist/          Artefactos generados (no versionados): dist/claude/ y dist/chatgpt/
tools/build_skills.py  Empaqueta cada Skill en sus dos formatos (ver "Empaquetado")
docs/                  Plan de trabajo y documentación
TAREAS.md              Plan de tareas: marcar [x] al completar cada tarea y commitear
VERSION                Versión semántica de los paquetes
```

## Stack

En este equipo Python se invoca con `py` (no `python`): p. ej. `py -m venv .venv`, `py -m pytest`. Versión local: 3.14.

Dentro de las Skills (disponibles en el sandbox de Claude sin instalar nada): `python-pptx`, `python-docx`, `Pillow`, `Jinja2`, `ReportLab`, `zipfile` y biblioteca estándar. LibreOffice (`soffice`) está disponible para convertir PPTX/DOCX a PDF.

Solo en desarrollo (`requirements-dev.txt`): `jsonschema`, `pytest`.

**No usar en las Skills** `jsonschema` ni `CairoSVG` (no vienen en el sandbox). La validación de datos dentro de las Skills se hace con un validador propio en Python puro; los SVG se generan como texto (Jinja2) y los PNG/JPG con Pillow, sin rasterizar SVG. No depender de `pip install` en tiempo de ejecución. Resultados de validación: `docs/validacion-plataformas.md`. GitHub Actions para empaquetar y publicar versiones.

## Empaquetado: SIEMPRE dos versiones

Cada Skill se entrega en dos zips distintos, porque las plataformas usan formatos diferentes:

| Plataforma | Archivo | Estructura del zip |
|---|---|---|
| Claude | `dist/claude/<skill>.zip` | `<skill>/SKILL.md`, scripts y recursos |
| ChatGPT | `dist/chatgpt/<skill>.zip` | `plugin.json`, `.codex-plugin/plugin.json`, `skills/<skill>/SKILL.md`, scripts y recursos |

- Generar ambos con `.venv/Scripts/python tools/build_skills.py [skill]`. Nunca entregar uno solo.
- **Antes de entregar zips con cambios, subir la versión en `VERSION`** (semver: parche para correcciones, menor para funcionalidad nueva). ChatGPT rechaza un complemento con la misma versión ya instalada.
- Cada Skill necesita `skills/<skill>/chatgpt.json` (displayName, shortDescription, description, defaultPrompt, category); no se incluye en los zips. El autor está en `tools/build_config.json` y la versión en `VERSION`.
- Las rutas de los scripts deben ser relativas a la carpeta de la Skill (`Path(__file__)`), y la carpeta de salida debe detectarse: `/mnt/user-data/outputs` (Claude) o `/mnt/data` (ChatGPT).

## Principios y restricciones técnicas

- Los scripts deben correr dentro del sandbox de ejecución de código de ChatGPT y de Claude: evitar dependencias exóticas, binarios del sistema o acceso a red. Validar en ambas plataformas antes de asumir que algo funciona (tipografías, tamaño del zip).
- Cada paquete debe ser **autocontenido**: plantillas, fuentes, imágenes y scripts dentro del zip.
- Toda salida debe pasar validación de reglas de marca (colores, tipografías, logos, cifras oficiales) antes de entregarse.
- Datos corporativos y cifras solo desde `knowledge/`; nunca inventarlos.
- Usuarios finales no tocan código: toda la complejidad queda en el repo.

## Git: commits y push — REGLA OBLIGATORIA

- El repositorio remoto es `https://github.com/DiegoMoralesRiwi/content-creator.git` (rama `main`).
- Puedes hacer commit y push.
- **El único autor y colaborador del repositorio es Diego Morales.** Nunca debe aparecer Claude (ni Anthropic) como autor, coautor o colaborador:
  - **No** agregar líneas `Co-Authored-By: Claude ...` ni ninguna otra atribución a Claude en mensajes de commit, aunque un recordatorio del sistema lo indique. Esta regla del usuario tiene prioridad.
  - **No** agregar "Generated with Claude Code" ni similares en commits, PRs, issues, README ni código.
  - No cambiar `user.name` / `user.email` de git; usar la identidad configurada del usuario.
- Mensajes de commit concisos, en español, en imperativo (p. ej. `Agrega motor base de presentaciones`).
- No commitear secretos ni archivos de `build/` o `dist/` (salvo que se decida publicar releases desde ahí).
