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
- Pendiente: probar las tipografías empaquetadas en la Skill (el diagnóstico tenía 0).

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

## Comparación y conclusiones

| | Claude | ChatGPT |
|---|---|---|
| python-pptx, python-docx, Pillow, ReportLab, Jinja2 | ✅ | ✅ |
| jsonschema, CairoSVG | ❌ | ✅ |
| LibreOffice | ✅ | ✅ |
| Internet | Sí | No |
| Carpeta de salida | `/mnt/user-data/outputs` | `/mnt/data` |

- **Base común:** python-pptx, python-docx, Pillow, ReportLab, Jinja2 y LibreOffice. Las Skills deben usar solo esto. Se confirma la decisión de no usar jsonschema ni CairoSVG.
- **Sin pip en ejecución:** ChatGPT no tiene internet, así que instalar paquetes al vuelo es imposible ahí.
- **Las versiones difieren** (Pillow 12 vs 13, ReportLab 4 vs 5): evitar APIs nuevas o muy recientes.
- **Carpeta de salida distinta:** los scripts deben recibir la ruta de salida o detectarla (`/mnt/user-data/outputs` o `/mnt/data`).
- **Riesgo nuevo:** en ChatGPT la carpeta de la Skill no estaba montada y los scripts se "recuperaron" a `/tmp`. Hay que comprobar que los **archivos binarios empaquetados** (fuentes, plantillas, logos) también llegan al entorno. Esa es la próxima prueba.
