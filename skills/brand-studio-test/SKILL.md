---
name: brand-studio-test
description: Skill de prueba técnica de Brand Studio. Úsala solo cuando el usuario pida "probar Brand Studio", "diagnóstico de Brand Studio" o "hola mundo de Brand Studio". Revisa el entorno de ejecución y genera una presentación PPTX de prueba.
---

# Brand Studio — prueba técnica

Esta Skill verifica que el entorno de ejecución de código de la plataforma (Claude o ChatGPT) puede correr los generadores de Brand Studio.

## Pasos

1. Ejecuta el diagnóstico desde la carpeta de esta Skill:

   ```bash
   python scripts/diagnostico.py
   ```

   Muestra al usuario el informe completo **tal cual**, sin resumirlo.

2. Si `python-pptx` está disponible, genera la presentación de prueba:

   ```bash
   python scripts/hola_pptx.py --salida brand_studio_prueba.pptx
   ```

   Si la plataforma tiene una carpeta para archivos descargables (por ejemplo `/mnt/user-data/outputs` o `/mnt/data`), guarda el archivo ahí. Entrega el archivo al usuario para descargar.

3. Si falta alguna librería, **no** la instales con pip salvo que el usuario lo pida; informa cuáles faltan. Esto es parte de lo que estamos midiendo.

No modifiques los scripts ni inventes resultados: el objetivo es medir el entorno real.
