# Distribución: límites y cómo compartir

Investigado el 2026-11-25. Verificar en la documentación oficial antes de depender de un dato, porque cambian.

## Límites

| | Claude | ChatGPT |
|---|---|---|
| Tamaño del paquete | **30 MB sin comprimir** por Skill ([docs de Anthropic](https://platform.claude.com/docs/en/build-with-claude/skills-guide)). Una fuente no oficial menciona 10 MB; usar 30 MB como referencia y vigilar | 780 MB por zip (pantalla de subida) |
| SKILL.md | Cuerpo recomendado: menos de 500 líneas ([buenas prácticas](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)) | Máximo 1 MiB (según Plugin Creator) |
| Descripción (frontmatter) | Máx. 1.024 caracteres; Claude.ai reportadamente limita a 200 | — |
| Nombre de carpeta | Debe coincidir con `name` del SKILL.md | — |

**Consecuencia:** el límite de Claude (30 MB) es el que manda. Cada Skill lleva los recursos de las tres marcas, así que hay que optimizar imágenes (PNG/JPG comprimidos, resolución justa), incluir solo los pesos tipográficos necesarios y evitar plantillas con imágenes pesadas. `tools/build_skills.py` falla si una Skill supera 30 MB sin comprimir.

## Cómo compartir con el workspace

### Claude (Team / Enterprise)

Fuente: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) y [Provisionar y administrar Skills para la organización](https://support.claude.com/zh-TW/articles/13119606).

- Subida: **Customize → Skills → + → Create skill → Upload a skill** (zip con la carpeta de la Skill).
- Las Skills subidas son privadas hasta que se comparten. Se pueden compartir con personas concretas y, en Enterprise, con grupos.
- Un propietario (owner) debe tener activados los interruptores de uso compartido de Skills (Skill sharing, Share with organization o Share with groups) para que aparezca el botón **Share**.
- **Opción recomendada:** los propietarios de Team y Enterprise pueden **provisionar** una Skill para toda la organización. Aparece en la lista de cada usuario con un indicador de equipo y cada uno puede activarla o desactivarla.
- Algunas versiones de la ayuda describen una biblioteca de la organización con revisión antes de publicar cada actualización: confirmar en la configuración real.

### ChatGPT (Business / Enterprise)

Fuente: [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt).

- Los miembros pueden compartir complementos si un administrador lo permite: **Workspace settings → Permissions & roles** (por rol).
- Opciones al compartir un complemento propio:
  - acceso para cualquiera del workspace que tenga el **enlace**;
  - publicarlo en el **directorio del workspace**, donde los miembros lo encuentran e instalan (no se publica en el directorio público).
- Los propietarios y administradores con permiso de subida pueden instalarlo para la organización: **Admin console → Plugins → Add** (subir el zip).
- Los nuevos complementos podrían estar desactivados por defecto según la configuración del workspace.
- Para usarlo, en el chat normal se puede llamar con `@` y el nombre del complemento.

## Pendiente de decidir

- Quién administra cada plataforma (necesitamos rol de owner/admin o apoyo de IT).
- Si se provisiona a toda la organización o solo a los equipos comercial y de mercadeo.
