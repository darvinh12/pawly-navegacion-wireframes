# Pendientes — Reto 11 (Pawly)

Lo que ya está en este repo cubre la parte local: árbol de navegación, arquitectura de información y wireframes mobile/desktop. Falta lo siguiente para cerrar el reto.

## 1. Figma

- Instalar el plugin `html.to.design` y correr el import de `wireframes/mobile.html` y `wireframes/desktop.html` (ver pasos ya acordados: `python -m http.server 5500` desde `wireframes/` y apuntar el plugin a `http://localhost:5500/...`).
- Convertir los bloques repetidos importados (avatar, card de publicación, card de mascota, botón, input) en **componentes** de Figma con Auto Layout.
- Organizar el archivo en páginas: `Cover`, `Components`, `Wireframes — Mobile`, `Wireframes — Desktop`, siguiendo el criterio del proyecto de ejemplo que dio la profesora.
- Trabajar esto en grupo (Figma es colaborativo en línea), no en solitario.

## 2. Pantallas no wireframeadas todavía

Quedaron fuera del set de 13 porque son variantes directas de otra pantalla ya cubierta. Agregarlas si el profesor pide una pantalla explícita por cada nodo del árbol de navegación:

- Recuperar contraseña (variante de Login).
- Perfil de otro usuario (variante de Mi perfil, en modo solo lectura).
- Feed de Socialización y detalle de mascota para socializar (mismo patrón que Adopción).
- Moderación de comentarios (mismo patrón que gestión de usuarios en Admin).
- HU-05: login de usuario migrado con CI como contraseña + forzar cambio en primer ingreso.

## 3. Exportables finales

- Exportar cada pantalla de Figma como imagen (PNG) para el Aula Virtual.
- Generar el PDF del entregable (mapa de navegación + wireframes + enlace a Figma).
- Subir imágenes + PDF al Aula Virtual, en el reto correspondiente.

## 4. Compartir y cerrar el reto

- Compartir el URL del proyecto de Figma con el grupo docente de ATI (`ati.ciencias.ucv@gmail.com`, y a quien más indique el enunciado).
- Colocar en el reto del Aula Virtual el enlace a este repositorio y el enlace de Figma.

## 5. Revisión técnica pendiente

- Confirmar si, tras terminar el diseño de pantallas en Figma, aparece algún dato no contemplado en `modelo_dominio.puml` del proyecto principal (Entrega 1). Hasta ahora no se detectó impacto.
- Decidir el mecanismo real de internacionalización (se sugirió en `arquitectura_informacion.md` usar archivos planos JSON por idioma) e implementarlo si el proyecto llega a esa etapa.
