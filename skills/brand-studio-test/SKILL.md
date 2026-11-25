---
name: brand-studio-test
description: Skill de prueba técnica de Brand Studio. Úsala solo cuando el usuario pida "probar Brand Studio", "diagnóstico de Brand Studio" o "hola mundo de Brand Studio". Revisa el entorno de ejecución, verifica los recursos empaquetados (fuente, plantilla, logo) y genera archivos de prueba.
---

# Brand Studio — prueba técnica

Esta Skill verifica que el entorno de ejecución de código de la plataforma (Claude o ChatGPT) puede correr los generadores de Brand Studio con los recursos empaquetados.

Todas las rutas son relativas a la carpeta de esta Skill (la que contiene este `SKILL.md`). Ejecuta los scripts **desde esa carpeta y sin copiarlos ni reescribirlos**. Si la carpeta no está accesible en el entorno de ejecución, dilo explícitamente en el informe (indica qué ruta intentaste y qué encontraste): es un resultado que necesitamos conocer.

## Pasos

1. Diagnóstico del entorno:

   ```bash
   python scripts/diagnostico.py
   ```

2. Prueba de recursos empaquetados (verifica fuente, plantilla y logo con sha256 y genera un PPTX y un PNG con ellos):

   ```bash
   python scripts/recursos.py
   ```

3. Presentación mínima de prueba:

   ```bash
   python scripts/hola_pptx.py --salida <carpeta de salida>/brand_studio_prueba.pptx
   ```

   La carpeta de salida es `/mnt/user-data/outputs` o `/mnt/data`, la que exista.

Muestra al usuario la salida de los pasos 1 y 2 **tal cual**, sin resumir, y entrega los tres archivos generados para descargar.

Si falta alguna librería o recurso, **no** lo instales ni lo reemplaces; informa qué falta. No modifiques los scripts ni inventes resultados: el objetivo es medir el entorno real.
