# Fase 2 — Recursos requeridos por marca

Se necesita **un juego completo por cada marca**: Riwi, Blackbird LATAM y Blackbird USA. Si dos marcas comparten algún recurso (por ejemplo, la tipografía de las dos Blackbird), entregarlo en ambas carpetas o indicarlo.

## Dónde dejarlos

```
brands/riwi/originales/
brands/blackbird-latam/originales/
brands/blackbird-usa/originales/
```

Se entregan los archivos originales, en la mejor calidad disponible. La optimización (tamaños, compresión, recortes) se hace después en el repositorio. Las Skills tienen un límite de 30 MB en total para las tres marcas, unos **8 MB por marca ya optimizados**.

Nombres de archivo: minúsculas, sin espacios ni tildes, con guiones. Ejemplo: `logo-principal-color.svg`.

## 1. Manual de marca — obligatorio

- **Formato:** PDF (o el que exista: PPTX, DOCX o enlace).
- Se usa como referencia para extraer las reglas; no se incluye en las Skills.

## 2. Logos — obligatorio

Cada variante en **dos formatos**:

| Formato | Especificación |
|---|---|
| **SVG** | Vectorial, con textos convertidos a trazos (curvas) |
| **PNG** | Fondo transparente, **mínimo 2000 px de ancho**, RGB |

> El PNG es imprescindible: en Claude y ChatGPT no hay forma de convertir SVG a imagen, así que las piezas usan el PNG.

Variantes (las que existan):

| Archivo | Uso |
|---|---|
| `logo-principal-color` | Versión principal, sobre fondo claro |
| `logo-negativo` | En blanco, para fondos oscuros o de color |
| `logo-monocromo-negro` | Una sola tinta negra |
| `logo-horizontal` / `logo-vertical` | Si hay versiones por orientación |
| `isotipo` | Solo el símbolo, sin texto (avatares, esquinas, favicon) |

Reglas que necesito saber (si el manual no las trae): tamaño mínimo, área de protección y fondos sobre los que **no** se puede usar.

## 3. Tipografías — obligatorio

- **Formato:** `.ttf` u `.otf`. No sirven WOFF/WOFF2 ni fuentes de Adobe Fonts sin archivo descargable.
- **Pesos:** solo los que se usan, máximo 4 por familia. Normalmente: Regular, Bold y, si aplica, SemiBold o Medium e Italic.
- **Licencia:** el archivo de licencia o confirmación de que permite incluir la fuente en las herramientas internas. Si es de Google Fonts, basta con el nombre.
- **Jerarquía:** qué fuente va en títulos, subtítulos y texto.
- **Fuente de respaldo para PowerPoint/Word**, por ejemplo Arial o Calibri.

> Los PPTX y DOCX no llevan la fuente incrustada: quien abra el archivo en un equipo sin la fuente verá la de respaldo. Las imágenes PNG/JPG sí salen siempre con la fuente correcta.

## 4. Colores — obligatorio

Por cada color: **nombre, HEX y RGB**, más su rol:

| Rol | Ejemplo |
|---|---|
| Primario | `#FF5C00` · 255, 92, 0 |
| Secundario(s) | |
| Acento | |
| Fondo claro / fondo oscuro | |
| Texto principal / texto secundario | |
| Degradados | Color inicial, color final y dirección |

También: combinaciones permitidas y prohibidas (texto sobre fondo) y proporción de uso, si la hay.

## 5. Plantilla de PowerPoint — obligatorio para Presentation Studio

- **Formato:** `.pptx` (o `.potx`).
- **Tamaño:** 16:9 (33,867 × 19,05 cm / 13,333 × 7,5 in).
- **Diseños del patrón**, en *Vista → Patrón de diapositivas*, usando **marcadores de posición** (no cuadros de texto sueltos):
  - Portada
  - Separador de sección
  - Título + contenido
  - Dos columnas
  - Imagen a pantalla completa con texto
  - Cifras o datos destacados
  - Cierre o contacto
- Colores y fuentes del tema configurados con los de la marca (*Diseño → Variantes*).
- Imágenes de fondo comprimidas: **archivo de menos de 5 MB**.
- Si existen presentaciones comerciales reales aprobadas, enviar 1 o 2 como referencia de estilo y estructura.

## 6. Plantilla de Word — obligatorio para propuestas y cotizaciones

- **Formato:** `.docx` (o `.dotx`).
- **Tamaño de página:** indicar **Carta o A4**. Si cambia por país (por ejemplo, Carta para USA y A4 para LATAM), decirlo.
- **Estilos definidos:** Título, Título 1, Título 2, Normal, Tabla y Pie de foto.
- Encabezado y pie con logo, datos de contacto y numeración.
- Si hay propuestas o cotizaciones reales aprobadas, enviar 1 o 2 como referencia, anonimizadas si tienen datos de clientes.

## 7. Redes sociales — obligatorio para Content Studio

Primero, **qué redes usa cada marca** (Instagram, LinkedIn, Facebook, TikTok, X).

Luego, ejemplos aprobados en **PNG o JPG**, de **3 a 5 por formato**:

| Formato | Tamaño (px) |
|---|---|
| Post cuadrado | 1080 × 1080 |
| Post vertical (Instagram/LinkedIn) | 1080 × 1350 |
| Historia / Reel (portada) | 1080 × 1920 |
| Carrusel (cada lámina) | 1080 × 1350 |
| Post horizontal LinkedIn | 1200 × 627 |
| Banner LinkedIn (empresa) | 1128 × 191 |
| Banner LinkedIn (personal) | 1584 × 396 |

Enviar solo los formatos que la marca use. También, si existen, las reglas de diseño: márgenes o zonas seguras, posición del logo, cuánto texto se permite y uso de hashtags y emojis.

## 8. Fotografías, fondos y texturas — opcional, recomendado

- **Formato:** JPG (fotos) y PNG (texturas con transparencia).
- **Tamaño:** lado mayor de 2000 a 2500 px.
- **Cantidad:** de 5 a 15 por marca, las más representativas.
- Solo imágenes con **derechos de uso** (propias o con licencia). Indicar si alguna requiere crédito.

## 9. Iconografía — opcional

- Si la marca tiene un set propio: **SVG** y **PNG de 512 × 512 px** con fondo transparente.
- Si usa un set público (por ejemplo, Phosphor o Material Symbols), basta con el nombre y el estilo (línea o relleno, grosor).

## 10. Datos básicos de cada marca — obligatorio

- Nombre comercial exacto y forma correcta de escribirlo (mayúsculas, espacios).
- Idioma o idiomas de comunicación (por ejemplo, Blackbird USA: inglés; Blackbird LATAM: español).
- Sitio web, redes oficiales y datos de contacto que pueden aparecer en las piezas.
- Eslogan o frases de marca aprobadas.

> La información de servicios, cifras, casos y tono de voz corresponde a la Fase 3.

## Resumen por marca

| # | Recurso | Formato | Obligatorio |
|---|---|---|---|
| 1 | Manual de marca | PDF | Sí |
| 2 | Logos (todas las variantes) | SVG + PNG ≥ 2000 px transparente | Sí |
| 3 | Tipografías + licencia + fuente de respaldo | TTF/OTF | Sí |
| 4 | Paleta de colores con roles | HEX + RGB | Sí |
| 5 | Plantilla PowerPoint 16:9 con patrón | PPTX < 5 MB | Sí |
| 6 | Plantilla Word con estilos | DOCX, Carta o A4 | Sí |
| 7 | Redes usadas + ejemplos aprobados | PNG/JPG en tamaños de la tabla | Sí |
| 8 | Fotos, fondos, texturas | JPG/PNG de 2000 a 2500 px | Recomendado |
| 9 | Iconos | SVG + PNG 512 px | Opcional |
| 10 | Datos básicos de la marca | Texto | Sí |
