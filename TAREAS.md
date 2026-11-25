# Brand Studio — Plan de tareas

Marcas: **Riwi**, **Blackbird LATAM**, **Blackbird USA**.
Leyenda: `[x]` lista · `[ ]` pendiente. Plan detallado: [docs/plan-de-trabajo.md](docs/plan-de-trabajo.md).

## Fase 0 — Configuración del proyecto

- [x] Analizar el plan de trabajo
- [x] Crear estructura base del repositorio
- [x] Crear `CLAUDE.md` con reglas del proyecto y de commits
- [x] Conectar el repositorio con GitHub (`main`)
- [x] Actualizar el plan a tres empresas (Riwi, Blackbird LATAM, Blackbird USA)
- [x] Python disponible en el equipo de desarrollo (3.14, se invoca con `py`)
- [x] Crear entorno virtual (`.venv`) e instalar `requirements.txt`
- [x] Configurar `pytest` y pruebas de humo del stack (`tests/test_entorno.py`)
- [x] CairoSVG descartado (no está en el sandbox); ya no hace falta cairo en Windows

## Fase 1 — Validación técnica en las plataformas (riesgo principal)

- [x] Crear una Skill mínima de prueba (`skills/brand-studio-test`: diagnóstico del entorno + PPTX)
- [x] Script de empaquetado `tools/build_skills.py` → `dist/<skill>.zip`
- [x] Probar la instalación y ejecución de la Skill en Claude (ver `docs/validacion-plataformas.md`)
- [ ] Probar la instalación y ejecución de la Skill en ChatGPT — **bloqueado: "Workspace plugin upload permission required"; un admin del workspace debe dar el permiso** (límite del zip: 780 MB)
- [ ] Verificar las librerías disponibles en cada sandbox (Claude ✅: faltan jsonschema y CairoSVG; ChatGPT pendiente)
- [x] Decidir el reemplazo de jsonschema y CairoSVG: validador propio + SVG como texto y Pillow; dependencias separadas en `requirements-dev.txt`
- [ ] Verificar que se usen las tipografías empaquetadas en la Skill
- [ ] Verificar el tamaño máximo del zip y los límites de archivos
- [ ] Verificar cómo se comparte una Skill con el espacio de trabajo en cada plataforma
- [ ] Documentar resultados y ajustar el stack si algo no funciona

## Fase 2 — Recursos de marca

Por cada marca: manual de identidad, logos, tipografías, colores, iconografía, imágenes y plantillas.

- [ ] Riwi: recopilar y organizar recursos en `brands/riwi/`
- [ ] Blackbird LATAM: recopilar y organizar recursos en `brands/blackbird-latam/`
- [ ] Blackbird USA: recopilar y organizar recursos en `brands/blackbird-usa/`
- [ ] Definir un esquema `brand.json` (colores, tipografías, logos, reglas) y validarlo (jsonschema en pruebas; validador propio en las Skills)
- [ ] Crear `brand.json` de cada marca
- [ ] Confirmar licencias de uso de las tipografías

## Fase 3 — Conocimiento corporativo

- [ ] Información corporativa de cada empresa (`knowledge/company-information/`)
- [ ] Catálogo de servicios de cada empresa (`knowledge/services/`)
- [ ] Reglas comerciales: precios, cotizaciones, condiciones (`knowledge/commercial-rules/`)
- [ ] Tono de voz e idiomas de cada marca (`knowledge/tone-of-voice/`)
- [ ] Cifras oficiales y casos de éxito aprobados

## Fase 4 — Motor de presentaciones (Presentation Studio)

- [ ] Diseñar el formato de entrada (JSON de contenido validado con un esquema)
- [ ] Generador de PPTX a partir de plantillas oficiales
- [ ] Generador de DOCX (propuestas y cotizaciones)
- [ ] Generador de PDF (one-pagers)
- [ ] Validador de reglas de marca para los documentos
- [ ] Pruebas automatizadas del motor
- [ ] Plantillas por marca: presentación comercial, propuesta, cotización, caso de éxito, one-pager

## Fase 5 — Motor de contenido (Content Studio)

- [ ] Diseñar el formato de entrada para piezas de redes
- [ ] Generador de posts (PNG/JPG)
- [ ] Generador de carruseles
- [ ] Generador de historias y banners
- [ ] Exportación SVG
- [ ] Validador de reglas de marca para imágenes
- [ ] Pruebas automatizadas del motor
- [ ] Plantillas de diseño aprobadas por marca

## Fase 6 — Skills

- [ ] Escribir `skills/presentation-studio/SKILL.md` (flujo conversacional, datos a pedir, selección de marca)
- [ ] Escribir `skills/content-studio/SKILL.md`
- [ ] Script de build que arme cada Skill autocontenida en `dist/`
- [ ] Probar ambas Skills de punta a punta en Claude
- [ ] Probar ambas Skills de punta a punta en ChatGPT

## Fase 7 — Automatización y versiones

- [ ] GitHub Action para correr las pruebas
- [ ] GitHub Action para empaquetar los zip y publicar un release por versión
- [ ] Definir la política de versiones (`VERSION`, changelog)

## Fase 8 — Despliegue y adopción

- [ ] Publicar las Skills en los espacios de trabajo corporativos de Claude y ChatGPT
- [ ] Guía rápida para comerciales y mercadeo
- [ ] Piloto con usuarios de cada empresa
- [ ] Recoger feedback y ajustar
