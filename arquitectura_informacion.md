# Reto 11 — Árbol de navegación, arquitectura de información y wireframes

Proyecto: Pawly (Red Social de Mascotas) · ATI 2026-1

## 1. Árbol de navegación

Ver `mapa_navegacion.puml` / `mapa_navegacion.png` / `mapa_navegacion.svg`. Construido a partir de los actores y casos de uso de `assets/casos_de_uso.puml` (Visitante, Usuario registrado/Dueño, Administrador) y de las historias del `backlog_github.csv`.

## 2. Tipos de página identificados

| Página | Actor(es) | Tipo |
|---|---|---|
| Landing / Iniciar sesión | Visitante | Formulario |
| Registro | Visitante | Formulario (wizard 2 pasos: datos básicos + perfil humano) |
| Recuperar contraseña | Visitante | Formulario |
| Feed / Muro (Inicio) | Usuario | Índice (listado homogéneo de publicaciones) |
| Detalle de publicación | Usuario | Detalle + índice anidado (comentarios) |
| Crear publicación | Usuario | Formulario (modal) |
| Buscar / Resultados | Usuario | Consulta + índice segmentado (usuarios / mascotas / publicaciones) |
| Feed de Adopción | Usuario | Índice filtrable |
| Detalle mascota en adopción | Usuario | Detalle + CTA (visita guiada hacia Chat) |
| Feed de Socialización | Usuario | Índice filtrable |
| Mensajes (lista) | Usuario | Índice |
| Conversación | Usuario | Detalle conversacional |
| Notificaciones | Usuario | Índice cronológico |
| Mi perfil (Humano) | Usuario | Detalle + índice anidado (mascotas, publicaciones) |
| Editar perfil humano | Usuario | Formulario |
| Perfil de mascota | Usuario | Detalle |
| Crear/editar mascota | Usuario | Formulario |
| Perfil de otro usuario | Usuario | Detalle (solo lectura + acciones: seguir, chat) |
| Panel de administración | Administrador | Dashboard (resumen + accesos) |
| Gestión de usuarios | Administrador | Índice + CRUD |
| Moderación (publicaciones/comentarios) | Administrador | Índice filtrable + acción de bloqueo |
| Reportes y veto | Administrador | Índice + detalle de reporte |

## 3. Unidades visuales por tipo de página

- **Header global** (autenticado): logo, buscador, íconos de Mensajes/Notificaciones, avatar con menú de cuenta.
- **Header público** (visitante): logo, enlaces Iniciar sesión / Registrarse.
- **Navegación principal**: bottom nav en mobile (5 ítems: Inicio, Buscar, Adopción/Socialización, Mensajes, Perfil), barra lateral o top nav en desktop.
- **Card de publicación**: avatar + nombre + fecha, texto, imagen opcional, acciones (comentar, etiquetas), contador de comentarios.
- **Card de mascota** (feed adopción/socialización): foto, nombre, especie/temperamento, distancia, botón de acción.
- **Card de usuario** (resultados de búsqueda, lista de seguidos): avatar, nombre/username, botón seguir.
- **Formulario**: campos agrupados, validación inline, botón primario de envío.
- **Bandeja de chat**: lista de conversaciones (avatar, último mensaje, hora, badge no leído) + panel de conversación (burbujas, input).
- **Panel de notificaciones**: lista cronológica con ícono por tipo (comentario, solicitud, chat).
- **Tabla de administración**: filas de usuarios/publicaciones/comentarios con acciones (editar, bloquear, vetar).
- **Footer**: solo en páginas públicas (landing/registro).

## 4. Elementos individuales recurrentes

Botón primario/secundario, enlace de texto, ícono (lupa, campana, sobre, corazón/seguir, adopción-pata, chat), título de sección, párrafo de descripción, campo de formulario (texto, fecha, selector especie/sexo, textarea, carga de imagen), avatar circular, badge de contador, barra de progreso (wizard de registro), chip de filtro (especie, cercanía), estrella/etiqueta de estado (pendiente/aceptada/rechazada).

## 5. Patrones de navegación

- **Índice**: feed principal, feed de adopción, feed de socialización, resultados de búsqueda, lista de chats, lista de mascotas propias, tabla de usuarios en administración. Todos son listados homogéneos con selección hacia un detalle.
- **Menú**: bottom nav (mobile) / barra superior o lateral (desktop) con 5 accesos fijos para el Usuario; el Administrador tiene un menú lateral propio con 4 secciones (Panel, Usuarios, Moderación, Reportes). No hay submenús desplegables; se prioriza navegación plana de un nivel para no perder al usuario (ver mapa de navegación, máximo 3 niveles de profundidad).
- **Visita guiada**: flujo de registro (datos básicos → perfil humano → opcional primera mascota) y flujo de postulación (ver mascota en adopción/socialización → confirmar solicitud → redirección automática al chat abierto con el dueño), reflejando el `<<include>>` de `UC_initchat` en el diagrama de casos de uso.
- **Consulta**: buscador único en el header global, visible en todas las páginas autenticadas, con resultados segmentados en pestañas (Usuarios / Mascotas / Publicaciones).

## 6. Preguntas de arquitectura de información

- **Áreas de contenido y servicio**: Muro social (publicaciones), Mascotas (perfiles y feeds de adopción/socialización), Mensajería, Administración/moderación.
- **Zona de navegación**: header fijo + bottom nav en mobile; header + sidebar fija en desktop. Persistente en todas las páginas autenticadas.
- **Sistemas de ayuda**: tooltips en íconos y texto de ayuda bajo campos de formulario (ej. explicación de "estaVetado", criterios de adopción); no se contempla un centro de ayuda separado en el MVP.
- **Formularios vs. listados**: formularios en Cuenta y acceso, Crear/editar mascota, Crear publicación, Editar perfil; listados en todo lo demás (feeds, búsqueda, mensajes, administración).

## 7. Diseño de interacción, navegación e interfaz

- **Interacción**: el usuario logra sus objetivos (postularse a adopción, socializar, chatear) en máximo 3 pasos desde el feed correspondiente; la apertura automática del chat al postularse (regla `<<include>>`) evita un paso manual extra.
- **Navegación**: sin enlaces externos salvo compartir (fuera de MVP); enlaces intra-page en el feed de notificaciones (saltan directo al comentario/chat referido); nombres de enlaces en lenguaje cercano al usuario ("Ver mascotas", "Mis chats", "Buscar amigos peludos" en vez de términos técnicos).
- **Interfaz**: iconografía de patas/huella para adopción y socialización, corazón para seguir, sobre para mensajes, campana para notificaciones. Metáfora de card para publicaciones y perfiles de mascota; carrusel para múltiples fotos de mascota.

## 8. Internacionalización

Textos de interfaz (labels, botones, mensajes de validación) no provienen del modelo de dominio y quedan sujetos a i18n: se recomienda externalizarlos en archivos planos JSON por idioma (`es.json` como default, `en.json` a futuro) en vez de guardarlos en BD, ya que no cambian por usuario. Los valores enumerados del dominio (`especie: perro/gato`, `tipo de solicitud`) si se traducen, requieren un diccionario de etiquetas asociado al enum, no cambio de modelo. No se identificó impacto que obligue a modificar `modelo_dominio.puml`.

## 9. Wireframes

Ver carpeta `wireframes/` — `mobile.html` (360×640, mobile first) y `desktop.html` (1440×1024), pantallas de bloque gris de baja fidelidad, una por cada tipo de página de la sección 2. Sirven de borrador local antes de pasar a Figma.
