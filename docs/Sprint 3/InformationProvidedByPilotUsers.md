# Análisis de costes
****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 22/04/2024           | Sprint 3          |


| MIEMBROS DEL EQUIPO DE TRABAJO | MIEMBROS DEL EQUIPO DE TRABAJO |
|--------------------------------|--------------------------------|
| Ignacio Arroyo Mantero         | Eloy Jiménez Medina            |
| Tadeo Cabrera Gómez            | Daniel Cortés Fonseca          |
| Andrés Jesús Somoza Sierra     | Fernando Baquero Fernández     |
| Pablo Pino Mateo               | Guillermo Gómez Romero         |
| Antonio Maqueda Acal           | Jesús Solís Ortega             |
| Gonzalo Ribas Luna             | Jaime García García            |
| Antonio Peláez Moreno          | Lucas Antoñanzas del Villar    |
| Álvaro Vázquez Conejo          | Raúl Hernán Mérida Bascón      |
| Ignacio González González      |                                |

****

## Criterios de aceptación establecidos

- **#1.** Ante la pregunta “¿Encontraste la aplicación fácil de usar? “, obtener una puntuación media entre 4 y 5. Fracaso es considerado entre 1 y 2. El resto de puntuación sería una valoración intermedia.
- **#2.** Ante la pregunta “¿Hubo algún elemento de la interfaz que te resultara confuso o difícil de entender?”, obtener menos de 5 incidencias diferentes.
- **#3.** Ante la pregunta “¿Has encontrado algún fallo?”, obtener 3 o menos errores diferentes.
- **#4.** Ante la pregunta “¿La aplicación respondió rápidamente a tus acciones?”, el criterio es el mismo que en la pregunta #1.
- **#5.** Ante la pregunta “En cuanto a estilos y diseño, ¿hay algo que no le gustase o que se pudiese cambiar?”, no hay resultados objetivo, simplemente es para tener en cuenta la opinión para plantear posibles mejoras.
- **#6.** Ante la pregunta “¿Alguna recomendación de mejora?”, no hay resultados objetivo, simplemente es para tener en cuenta la opinión para plantear posibles mejoras.

**Criterio** | **#1** | **#2** | **#3** | **#4** | **#5** | **#6**
--- | --- | --- | --- | --- | --- | ---
**Alcanzado** | Sí | Sí | No | Sí | N/A | N/A

## Análisis de criterios de aceptación establecidos
- **¿Encontraste la aplicación fácil de usar?**  
Se ha obtenido una puntuación media de 3.91
- **¿Hubo algún elemento de la interfaz que te resultara confuso o difícil de entender?**
  - Inicio de Sesión: Sugieren un arreglo en el uso de las solicitudes para iniciar sesión.
  - Aceptación de solicitudes: Confusión respecto a la confirmación a la hora de aceptar solicitudes.
  - Calendario:  Una persona no entendio muy bien el funcionamiento total del calendario.
  - Documentos: No se distinguían bien los documentos según su importancia.

- **¿Has encontrado algún fallo?**
  - Funcionalidad General: Se ha observado el salto de un error 500 a la hora de editar un documento en estado de aportaciones.
  - Formularios y Campos de Texto: Se ha identificado la posibilidad de escribir textos demasiado largos en diversos campos, lo que causa problemas de visualización y puede afectar la usabilidad. Los campos de número de teléfono no validan correctamente las entradas, lo que puede resultar en datos incorrectos o incompletos sin una indicación clara para el usuario. 
  - Registro y Creación de Solicitudes: El filtrado de estas no funciona bien. 
  - Edición y Validación de Datos: Se han identificado errores en la validación de datos al crear eventos y mensajes de chat muy largos, incluyendo la posibilidad de introducir caracteres no válidos y la falta de indicaciones claras sobre los formatos esperados.

- **¿La aplicación respondió rápidamente a tus acciones?**  
Se ha obtenido para este apartado una puntuación media de 4.3.
- **En cuanto a estilos y diseño, ¿hay algo que no le gustase o que se pudiese cambiar?**
  - Interfaz General: Se detecto la sugerencia de una persona de rellenar algunas partes de la interfaz para que no sea tan blanca.
  - Diseño de Documentos: Fallo visual en los comentarios de los mismos.
  - Mejoras Generales: Algunos textos se salen de los recuadros. Pantalla de chat más llamativa.

- **¿Alguna recomendación de mejora?**
  - Idioma y Realismo de Datos: Revisar y traducir completamente la interfaz al español para una experiencia más coherente y accesible para todos los usuarios. Implementar validaciones más estrictas en los campos de entrada, como números de teléfono y números de licencia, para garantizar datos más realistas y útiles en la base de datos. 
  - Gestión de Mensajes de Chat: Mejorar la interfaz de este y hacer que los mensajes salten de página y no se vean en una misma línea.
  - Filtrado y Gestión de Contenidos: Agregar opciones de filtrado por estado de solicitud en la pantalla de Solicitudes para facilitar la búsqueda y gestión de solicitudes pendientes o en proceso. Incluir un aviso de confirmación antes de eliminar documentos u otros elementos importantes para prevenir errores accidentales y la pérdida de datos. 
  - Manual de usuario: Proporcionar un mejor manual de usuario para que puedan acudir a él cuando se encuentren problemas.

## Conclusión
- Se han superado los criterios de aceptación de tres de las preguntas, y otra con un intervalo intermedio, con algunas áreas de mejora en la usabilidad y funcionalidad.
- Se destaca la necesidad de mejorar la claridad en la interfaz, especialmente en áreas como el inicio de sesión, los comentarios de documentos y el chat.
- Se sugiere una revisión exhaustiva de la aplicación, incluyendo la traducción completa al español y la implementación de validaciones más estrictas en los campos de entrada.
- Las recomendaciones de mejora incluyen la optimización de la experiencia del usuario en la edición de documentos, la gestión de solicitudes y el uso del chat de una manera más visual.





