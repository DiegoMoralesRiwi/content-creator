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
- **jsonschema y CairoSVG no están en el entorno.** Instalarlos con pip en cada conversación es lento y depende de la red. Opciones:
  - jsonschema: usarlo solo en desarrollo y escribir un validador propio y ligero dentro de las Skills.
  - CairoSVG: generar los SVG como texto (con Jinja2) y los PNG/JPG con Pillow, sin rasterizar SVG.
- LibreOffice está disponible, así que se pueden generar PDF convirtiendo el PPTX o el DOCX, como alternativa a ReportLab.
- Pendiente: probar las tipografías empaquetadas en la Skill (el diagnóstico tenía 0).

## ChatGPT

Bloqueado: la instalación de Skills requiere permiso de IT. Pendiente.
