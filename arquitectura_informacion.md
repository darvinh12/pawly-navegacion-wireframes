# Reto 11 — Árbol de navegación, arquitectura de información y prototipos

Proyecto: Pawly (Red Social de Mascotas) · ATI 2026-1

Funcionalidad núcleo elegida por el equipo: **Adopciones**. De las tres funcionalidades parecidas del enunciado (adopción, pareja y socialización), el MVP del equipo cubre solo adopción. El árbol de navegación, las pantallas y el modelo quedan acotados a ese alcance.

## 1. Árbol de navegación

Ver `mapa_navegacion.puml` / `mapa_navegacion.png` / `mapa_navegacion.svg`. Construido a partir de los actores y casos de uso de `assets/casos_de_uso.puml` (Visitante, Usuario registrado/Dueño, Administrador) y de las historias del `backlog_github.csv`, dejando fuera las historias de socialización (HU-25 a HU-27).

## 2. Tipos de página identificados

| Página | Actor(es) | Tipo |
|---|---|---|
| Landing / Iniciar sesión | Visitante | Formulario |
| Registro | Visitante | Formulario (wizard 2 pasos: cuenta + perfil humano) |
| Recuperar contraseña | Visitante | Formulario |
| Feed / Muro (Inicio) | Usuario | Índice (listado homogéneo de publicaciones) |
| Detalle de publicación | Usuario | Detalle + índice anidado (comentarios) |
| Crear publicación | Usuario | Formulario (compositor en el feed) |
| Buscar / Resultados | Usuario | Consulta + índice segmentado (usuarios / mascotas / publicaciones) |
| Feed de Adopción | Usuario | Índice filtrable por especie, edad y cercanía |
| Detalle mascota en adopción | Usuario | Detalle + CTA (visita guiada hacia Chat) |
| Postulación | Usuario | Formulario corto (bottom sheet en mobile, modal en desktop) |
| Mensajes (peticiones + lista) | Usuario | Índice |
| Conversación | Usuario | Detalle conversacional |
| Notificaciones | Usuario | Índice cronológico |
| Mi perfil (Humano) | Usuario | Detalle + índices anidados (mascotas, publicaciones, postulaciones) |
| Editar perfil humano | Usuario | Formulario |
| Perfil de mascota | Usuario | Detalle |
| Crear/editar mascota | Usuario | Formulario (incluye el bloque "Poner en adopción") |
| Perfil de otro usuario | Usuario | Detalle (solo lectura + acciones: seguir, chat) |
| Panel de administración | Administrador | Dashboard (indicadores + reportes pendientes) |
| Gestión de usuarios | Administrador | Índice + CRUD |
| Moderación (publicaciones/comentarios) | Administrador | Índice filtrable + acción de bloqueo |
| Reportes y veto | Administrador | Índice + detalle de reporte |

## 3. Unidades visuales por tipo de página

- **Barra superior** (autenticado): logo, buscador global, íconos de Notificaciones y Mensajes con contador, avatar.
- **Barra superior pública** (visitante): logo y enlace a Iniciar sesión / Crear cuenta.
- **Navegación principal**: barra inferior en mobile con 5 accesos (Inicio, Buscar, Adopción destacado al centro, Mensajes, Perfil); barra lateral fija en desktop con los mismos accesos más Notificaciones y el botón Publicar.
- **Card de publicación**: avatar, nombre, usuario, ubicación y fecha; texto; imagen opcional; acciones (me gusta, comentar); etiqueta "En adopción" cuando corresponde.
- **Card de mascota** (feed de adopción, perfil): foto 4:3, distancia, nombre, especie, edad y sexo.
- **Card de usuario** (resultados de búsqueda, sugerencias): avatar, nombre, usuario, ciudad y botón Seguir.
- **Formulario**: campos agrupados con etiquetas, texto de ayuda, selectores segmentados (especie, sexo), chips (temperamento), campo de fecha, interruptor (poner en adopción).
- **Bandeja de chat**: bloque de peticiones (aceptar / rechazar) y lista de conversaciones con último mensaje, hora y contador; en desktop, panel dividido con la conversación al lado.
- **Conversación**: mensaje de sistema que indica que el chat se abrió por una postulación, burbujas propias y ajenas con hora, campo de envío.
- **Lista de notificaciones**: ícono por tipo (adopción, comentario, petición, seguidor), texto, tiempo y acción rápida.
- **Tablas y tarjetas de administración**: indicadores, tabla de usuarios con estado y acciones (editar, vetar, eliminar), tarjetas de reportes con acción de bloqueo o veto.

## 4. Elementos individuales recurrentes

Botón primario (terracota), secundario (contorno), oscuro y de peligro; enlace de texto; íconos lineales (casa, lupa, huella, burbuja, campana, persona, corazón, pin, filtro, calendario, cámara, escudo, bandera); títulos en Bricolage Grotesque; texto en Figtree; campo de texto, área de texto, campo de fecha, selector segmentado, chip, interruptor; avatar circular; etiqueta de estado (En adopción, Activa, Reportes, Vetada); contador numérico; barra de progreso del registro.

## 5. Patrones de navegación

- **Índice**: feed principal, feed de adopción, resultados de búsqueda, lista de chats, notificaciones, mascotas propias, tabla de usuarios y tarjetas de reportes.
- **Menú**: barra inferior (mobile) o lateral (desktop) con accesos fijos para el Usuario; menú lateral propio del Administrador (Panel, Usuarios, Publicaciones, Comentarios, Reportes). Sin submenús: navegación plana con un máximo de tres niveles de profundidad.
- **Visita guiada**: registro en dos pasos (cuenta, luego perfil humano) y postulación a adopción (ver mascota, confirmar postulación con un mensaje, redirección automática al chat abierto con el dueño), que refleja el `<<include>>` de `UC_initchat` en el diagrama de casos de uso.
- **Consulta**: buscador único en la barra superior, visible en todas las páginas autenticadas, con resultados por pestañas (Usuarios, Mascotas, Publicaciones). En el feed de adopción hay además filtros por especie, edad y distancia.

## 6. Preguntas de arquitectura de información

- **Áreas de contenido y servicio**: Muro social (publicaciones y comentarios), Mascotas (perfiles y feed de adopción), Mensajería, Notificaciones, Administración y moderación.
- **Zona de navegación**: barra superior más barra inferior en mobile; barra superior más lateral fija en desktop. Persistente en todas las páginas autenticadas.
- **Sistemas de ayuda**: textos de ayuda bajo los campos de formulario, mensajes de sistema dentro del chat y avisos contextuales (por ejemplo "Se abrirá un chat con Carlos"). No se contempla un centro de ayuda separado en el MVP.
- **Formularios vs. listados**: formularios en Cuenta y acceso, Editar perfil, Crear/editar mascota, Postulación; listados en todo lo demás.

## 7. Diseño de interacción, navegación e interfaz

- **Interacción**: postularse a una adopción toma tres toques desde el feed de adopción (abrir mascota, postularme, enviar). La apertura automática del chat evita un paso manual. La postulación se puede cancelar desde el mismo chat.
- **Navegación**: sin enlaces externos en el MVP; las notificaciones enlazan directo al chat, comentario o mascota referida; nombres en lenguaje cercano ("Postularme para adoptar", "Ver a Toby", "Personas que quizá conoces").
- **Interfaz**: huella como ícono de Adopción y del logo; corazón para guardar; burbuja para mensajes; campana para notificaciones. Cards para publicaciones y mascotas; galería de miniaturas en el detalle de la mascota; bottom sheet en mobile y modal en desktop para la postulación.

## 8. Sistema visual del prototipo

- **Tipografía**: Bricolage Grotesque (titulares, 600 a 800) y Figtree (texto, 400 a 700). Ambas en Google Fonts y disponibles en Figma.
- **Color**: fondo crema `#FBF7F2`, superficie `#FFFDFA`, texto `#1F1A17`, texto secundario `#7A6F68`, acento terracota `#E8683A` (acciones principales y adopción), verde `#3F7D5A` para estados positivos, ámbar y rojo para moderación.
- **Radios**: 8, 14 y 20 px, más píldora para botones y chips.
- **Retícula**: mobile a una columna sobre 360 px con márgenes de 16 px; desktop sobre 12 columnas en 1440 px, con barra lateral de 240 px, contenido central de 680 px y columna auxiliar de 320 px. En mobile la columna auxiliar se oculta y la barra lateral se convierte en barra inferior.

## 9. Datos del modelo en pantalla

Las pantallas muestran los atributos del `modelo_dominio.puml`: `Usuario` (username, email), `PerfilHumano` (nombre, foto, ci, fechaNacimiento, genero, descripcion, ciudad), `PerfilMascota` (nombre, especie, sexo, temperamento, fechaNacimiento, descripcion, foto, enAdopcion), `Publicacion`, `Comentario`, `Solicitud` (tipo adopción, estado, caracteristicasBuscadas), `Chat`, `Mensaje`, `Notificacion` y `Administrador`. Las fechas se presentan como fechas (campo con calendario en formularios, formato corto en listados) y no como texto libre.

## 10. Internacionalización

Los textos de interfaz (etiquetas, botones, mensajes de ayuda y de sistema) no provienen del modelo de dominio y quedan sujetos a i18n. Se recomienda externalizarlos en archivos planos JSON por idioma (`es.json` por defecto, `en.json` a futuro) en lugar de guardarlos en base de datos, porque no varían por usuario. Los valores enumerados del dominio (`especie`, `sexo`, `tipo` y `estado` de la solicitud) se traducen con un diccionario de etiquetas asociado al enum. No se detectó impacto que obligue a modificar el modelo, salvo eliminar del alcance del MVP los valores `pareja` y `socializar` del enum `tipo` de `Solicitud` y los booleanos `buscaPareja` y `buscaSocializar` de `PerfilMascota`.

## 11. Prototipos

Carpeta `prototipo/`: `mobile.html` (Android 360×640, 14 pantallas) y `desktop.html` (1440×1024, 13 pantallas), construidos con `estilos.css` como sistema de diseño compartido. Las imágenes exportadas de cada pantalla están en `prototipo/export/`. La carpeta `wireframes/` conserva la versión de baja fidelidad previa como referencia del proceso.
