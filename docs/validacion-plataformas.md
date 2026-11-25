# Validación técnica en las plataformas

Resultados de la Skill `brand-studio-test` (Fase 1).

## Claude — 2026-11-25

Instalación y ejecución correctas. El PPTX de prueba se generó y quedó disponible para descargar.

| Aspecto | Resultado |
|---|---|
| Python | 3.12.3, Linux x86_64 |
| Ruta de la Skill | `/mnt/skills/plugins/brand-studio-test` (con permiso de escritura) |
| Salida descargable | `/mnt/user-data/outputs` |
| python-pptx | 1.0.2 ✅ |
| python-docx | 1.2.0 ✅ |
| Pillow | 13.0.0 ✅ |
| ReportLab | 5.0.1 ✅ |
| Jinja2 | 3.1.6 ✅ |
| jsonschema | ❌ no instalado |
| CairoSVG | ❌ no instalado |
| LibreOffice (`soffice`) | ✅ permite convertir PPTX/DOCX a PDF |
| ImageMagick (`convert`), `fc-list` | ✅ |
| `rsvg-convert`, `inkscape` | ❌ |
| Fuentes del sistema | 187 |
| Internet | Sí (pypi.org). No se debe depender de esto: puede cambiar según la configuración de la organización |

### Implicaciones

- **Funcionan sin instalar nada:** PPTX, DOCX, PDF e imágenes PNG/JPG.
- **jsonschema y CairoSVG no están en el entorno.** Decisión (2026-11-25): no usarlos dentro de las Skills.
  - jsonschema: usarlo solo en desarrollo y escribir un validador propio y ligero dentro de las Skills.
  - CairoSVG: generar los SVG como texto (con Jinja2) y los PNG/JPG con Pillow, sin rasterizar SVG.
- LibreOffice está disponible, así que se pueden generar PDF convirtiendo el PPTX o el DOCX, como alternativa a ReportLab.
- **Recursos empaquetados (v0.2.0) ✅:** la carpeta de la Skill está en `/mnt/skills/plugins/<skill>`. Fuente, plantilla PPTX y logo llegaron intactos (sha256 coincide). Pillow cargó la fuente empaquetada y se generaron el PPTX (plantilla + logo) y el PNG (logo + fuente) en `/mnt/user-data/outputs`.
- **No escribir en la carpeta de la Skill:** aunque el diagnóstico la reporta con permiso de escritura, Claude indica que debe tratarse como de solo lectura. Los archivos temporales y de salida van en la carpeta de salida o en `/tmp`.

## ChatGPT — 2026-11-25

Instalado como complemento (tras resolver el permiso del workspace). El PPTX de prueba se generó y se pudo descargar (2 diapositivas, 28,7 KB).

| Aspecto | Resultado |
|---|---|
| Python | 3.13.5, Linux x86_64 |
| Ruta de la Skill | **No montada**: ChatGPT copió los scripts a `/tmp/brand-studio-test` para ejecutarlos |
| Salida descargable | `/mnt/data` |
| python-pptx | 1.0.2 ✅ |
| python-docx | 1.2.0 ✅ |
| Pillow | 12.3.0 ✅ |
| ReportLab | 4.4.9 ✅ |
| Jinja2 | 3.1.6 ✅ |
| jsonschema | 4.26.0 ✅ |
| CairoSVG | 2.8.2 ✅ |
| LibreOffice, ImageMagick, `fc-list`, Inkscape | ✅ |
| `rsvg-convert` | ❌ |
| Fuentes del sistema | 2390 |
| Internet | **No** |

### Prueba de recursos (v0.2.0) — ❌ bloqueada

El complemento se instala y ChatGPT puede leer `SKILL.md` y ve en su catálogo los scripts, la fuente, la plantilla y el logo. Pero **esos archivos no existen en el entorno de ejecución de código**: se buscó en `/home/oai/skills/`, `/mnt/skills/`, `/skills/`, `/mnt/`, `/tmp/`, `/opt/` y en todo el sistema de archivos, sin resultados. Como la Skill prohíbe copiar o reescribir los scripts, no se generó ningún archivo (0 de 3).

En la primera prueba (v0.1.0) los scripts sí corrieron porque ChatGPT los leyó del catálogo y los **reescribió** en `/tmp`. Eso funciona con texto, pero no sirve para archivos binarios (fuentes, plantillas, logos) y el modelo podría alterar el código.

La documentación de OpenAI sobre complementos describe `scripts/` y `assets/` dentro de las Skills, pero no explica cómo llegan al entorno de ejecución ni ofrece un campo del manifiesto para montarlos ([skills](https://developers.openai.com/plugins/build/skills), [plugins](https://developers.openai.com/plugins/build/plugins)).

**Conclusión:** hoy, un complemento de ChatGPT no sirve para entregar recursos de marca binarios al entorno de ejecución. Hay que buscar otro canal para ChatGPT.

### Complemento creado con Plugin Creator (v0.2.0/0.2.1) — ✅ recursos accesibles

Se subió el zip a través de **Plugin Creator** (chat de creación de complementos). El complemento se ejecutó en un entorno distinto al de la primera prueba (tipo agente/"Work"):

| Aspecto | Resultado |
|---|---|
| Python | 3.12.14 |
| Ruta de la Skill | `/home/agent/.codex/plugins/cache/workspace-shared-with-me/<plugin>/<versión>/skills/<skill>` (**solo lectura**) |
| Carpeta de salida | `/workspace/scratch/<id>/...` (no existen `/mnt/data` ni `/home/oai/skills`) |
| python-pptx, python-docx, Pillow 13, ReportLab 4.4.9 | ✅ |
| **Jinja2** | ❌ no instalado |
| jsonschema | ✅ · CairoSVG ❌ |
| `soffice` ✅ · `libreoffice` ❌ · `fc-list`, `convert`, `inkscape` ✅ | |
| Fuentes del sistema | 368 |
| Internet | No |
| Recursos empaquetados | ✅ fuente, plantilla y logo intactos (sha256); PPTX y PNG generados |

Observaciones:

- Plugin Creator actualizó el complemento a **0.2.1** por su cuenta. Las próximas entregas deben usar una versión mayor (0.3.0).
- La ruta depende del entorno y de la versión: los scripts deben resolver todo desde `__file__` (ya lo hacen).
- Falta confirmar que una **conversación nueva** cargue el complemento y ejecute el flujo con «Probar Brand Studio».
- Plugin Creator sugiere, si algún entorno no da acceso a los archivos, un servidor MCP propio. Se descarta por ahora: requiere hosting (contradice el costo $0).

## Comparación y conclusiones

| | Claude | ChatGPT |
|---|---|---|
| python-pptx, python-docx, Pillow, ReportLab, Jinja2 | ✅ | ✅ |
| jsonschema, CairoSVG | ❌ | ✅ |
| LibreOffice | ✅ | ✅ |
| Internet | Sí | No |
| Carpeta de salida | `/mnt/user-data/outputs` | `/mnt/data` |

- **Base común (actualizada tras la prueba con Plugin Creator):** python-pptx, python-docx, Pillow, ReportLab y LibreOffice (`soffice`). **Jinja2 no está en todos los entornos**: no usarlo en las Skills. jsonschema y CairoSVG tampoco.
- **Sin pip en ejecución:** ChatGPT no tiene internet, así que instalar paquetes al vuelo es imposible ahí.
- **Las versiones difieren** (Pillow 12 vs 13, ReportLab 4 vs 5): evitar APIs nuevas o muy recientes.
- **Carpeta de salida distinta:** los scripts deben recibir la ruta de salida o detectarla (`/mnt/user-data/outputs` o `/mnt/data`).
- **Riesgo nuevo:** en ChatGPT la carpeta de la Skill no estaba montada y los scripts se "recuperaron" a `/tmp`. Hay que comprobar que los **archivos binarios empaquetados** (fuentes, plantillas, logos) también llegan al entorno. Esa es la próxima prueba.
