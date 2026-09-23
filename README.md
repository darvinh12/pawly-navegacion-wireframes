# Pawly — Árbol de navegación y prototipos de alta fidelidad

Reto 11 de ATI (2026-1), proyecto **Pawly** (red social de mascotas). Funcionalidad núcleo del equipo: **Adopciones**.

## Contenido

- `mapa_navegacion.puml` / `.png` / `.svg` — árbol de navegación por actor (Visitante, Usuario registrado, Administrador), a partir de los casos de uso y el Product Backlog del proyecto.
- `arquitectura_informacion.md` — tipos de página, unidades visuales, elementos, patrones de navegación, sistema visual, datos del modelo en pantalla e internacionalización.
- `prototipo/` — prototipos de alta fidelidad en HTML/CSS:
  - `mobile.html` — Android 360×640, 14 pantallas (mobile first).
  - `desktop.html` — 1440×1024, 13 pantallas.
  - `estilos.css` — sistema de diseño compartido (tipografía, color, componentes).
  - `export/` — una imagen PNG por pantalla, listas para entregar.
  - `exportar_pantallas.py` — recorta las pantallas a partir de una captura completa de la galería.
- `wireframes/` — versión de baja fidelidad previa, conservada como referencia del proceso.

## Cómo verlo

Abrir `prototipo/mobile.html` o `prototipo/desktop.html` en el navegador. Las fuentes se cargan desde Google Fonts (Bricolage Grotesque y Figtree); sin conexión se usa la fuente de respaldo del sistema.

## Regenerar las imágenes

Con el navegador automatizado (`agent-browser`) abierto en la galería y una captura completa (`--full`) guardada, ejecutar:

```
python exportar_pantallas.py _full_desktop.png rects_desktop.json desktop export
python exportar_pantallas.py _full_mobile.png rects_mobile.json mobile export
```

`rects.json` es la lista de posiciones de cada `.frame` (id, x, y, w, h, label) en coordenadas de documento.

## Proyecto principal

El código y el resto de entregas de Pawly viven en la organización [Pawly-ATI-UCV](https://github.com/orgs/Pawly-ATI-UCV/repositories). Este repositorio es material de apoyo para el diseño de navegación e interfaz.
