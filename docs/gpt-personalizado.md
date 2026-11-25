# Prueba: GPT personalizado en ChatGPT

Los complementos de ChatGPT no entregan sus archivos al entorno de ejecución de código (ver `validacion-plataformas.md`). Esta prueba usa un **GPT personalizado**: los archivos de conocimiento de un GPT quedan disponibles para el código en `/mnt/data`.

## Archivos

Se generan con `.venv/Scripts/python tools/build_skills.py brand-studio-test`:

- `dist/gpt/brand-studio-test/brand-studio-test.zip`: la Skill completa (scripts, fuente, plantilla y logo).
- `dist/gpt/brand-studio-test/instrucciones.txt`: las instrucciones del GPT. Empiezan con un bloque de arranque que descomprime el zip en `/tmp/brand-studio-test/` y después siguen las de `SKILL.md`.

## Configuración en ChatGPT

1. Explorar GPTs → **Crear** → pestaña **Configurar**.
2. **Nombre:** Brand Studio Test.
3. **Instrucciones:** pegar todo el contenido de `instrucciones.txt`.
4. **Iniciadores de conversación:** `Probar Brand Studio`.
5. **Conocimiento:** subir `brand-studio-test.zip`.
   - Si ChatGPT rechaza el zip, anotarlo como resultado de la prueba.
6. **Capacidades:** activar **Code Interpreter y análisis de datos**. Las demás no hacen falta.
7. **Crear** → compartir **solo conmigo** durante la prueba.
8. En una conversación nueva con el GPT: `Probar Brand Studio`.

## Qué se mide

- Si el zip aparece en `/mnt/data` y se descomprime.
- Si los recursos llegan intactos (sha256) y se generan el PPTX y el PNG.
- Si los archivos generados se pueden descargar.
- Si el GPT se puede compartir con el workspace (paso posterior).
