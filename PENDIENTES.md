# Pendientes — Reto 11 (Pawly)

Lo que ya está en este repo: árbol de navegación acotado a Adopciones, arquitectura de información, prototipos de alta fidelidad mobile y desktop en HTML/CSS y las imágenes PNG de cada pantalla. Falta lo siguiente para cerrar el reto.

## 1. Figma

- Instalar el plugin `html.to.design` y correr el import de `prototipo/mobile.html` y `prototipo/desktop.html` (levantar `python -m http.server 5500` desde `prototipo/` y apuntar el plugin a `http://localhost:5500/mobile.html` y `http://localhost:5500/desktop.html`).
- Confirmar que Figma resuelve las fuentes Bricolage Grotesque y Figtree (ambas están en Google Fonts dentro de Figma).
- Convertir los bloques repetidos en **componentes** con Auto Layout: barra superior, barra inferior, barra lateral, card de publicación, card de mascota, card de usuario, botón, campo de formulario, chip, etiqueta de estado, burbuja de chat, ítem de notificación.
- Crear la página `Estilos` con los estilos de texto y color tomados de `prototipo/estilos.css` (sección 8 de `arquitectura_informacion.md`).
- Organizar el archivo en páginas: `Portada`, `Componentes`, `Estilos`, `Mobile`, `Desktop`.
- Trabajar el archivo en equipo dentro del team de Figma.

## 2. Cobertura de casos de uso

Todos los casos de uso del Product Backlog (UC-01 a UC-31, menos UC-19 a UC-21 de socialización) tienen pantalla en el prototipo; la tabla de trazabilidad está en la sección 12 de `arquitectura_informacion.md`. Variantes que se pueden agregar en Figma si el profesor pide una pantalla por cada nodo del árbol:

- Perfil de mascota propia y de otro usuario (variante del detalle de mascota en adopción, sin el botón de postulación).
- Moderación de publicaciones y de comentarios en Admin como pestañas propias (mismo patrón que la tabla de usuarios).
- Pantalla de "Cambiar contraseña" al primer ingreso de un usuario migrado (hoy está resuelto dentro de Ajustes).

## 3. Exportables finales

- Las imágenes PNG de cada pantalla ya están en `prototipo/export/`. Si se editan las pantallas en Figma, exportar de nuevo desde Figma para que coincidan.
- Generar el PDF del entregable: mapa de navegación, resumen de la arquitectura de información, pantallas mobile y desktop, enlace a Figma.
- Subir imágenes + PDF al Aula Virtual en el reto correspondiente.

## 4. Compartir y cerrar el reto

- Compartir el URL del proyecto de Figma con el grupo docente de ATI (`ati.ciencias.ucv@gmail.com` y a quien más indique el enunciado).
- Colocar en el reto del Aula Virtual el enlace a este repositorio y el enlace de Figma.

## 5. Revisión técnica pendiente

- Actualizar `modelo_dominio.puml` de la Entrega 1 para reflejar el alcance de Adopciones: dejar solo `adopcion` en el enum `tipo` de `Solicitud` y quitar `buscaPareja` y `buscaSocializar` de `PerfilMascota`.
- Actualizar `casos_de_uso.puml` de la Entrega 1: el caso "Marcar mascota (adopción / pareja / socializar)" pasa a "Marcar mascota en adopción" y desaparecen "Enviar solicitud de pareja" y "Enviar solicitud de socialización".
- Cerrar o marcar fuera de alcance en el Product Backlog de GitHub las historias HU-25, HU-26 y HU-27 (socialización).
- Decidir el mecanismo real de internacionalización (archivos JSON por idioma) e implementarlo si el proyecto llega a esa etapa.
