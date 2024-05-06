# Análisis de costes
****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 06/05/2024           | PPL               |


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
**Alcanzado** | Sí | No | No | Sí | N/A | N/A

## Análisis de criterios de aceptación establecidos
- **¿Encontraste la aplicación fácil de usar?**  
Se ha obtenido una puntuación media de 4
- **¿Hubo algún elemento de la interfaz que te resultara confuso o difícil de entender?**
  - Calendario:  Una persona no entendió las actividades del calendario, y varias tienen dificultades con el tamaño de este. 

- **¿Has encontrado algún fallo?**
  - Funcionalidad General: Se ha observado el salto de un error 500 a la hora de editar un documento en estado de aportaciones. 

  - Formularios y Campos de Texto: A pesar de que las contraseñas se piden que tengan 8 caracteres en el frontend, en el backend el validador pide 12. Además, el nombre de un documento suficiente largo puede alterar la interfaz. 

  - Edición y Validación de Datos: Se han identificado errores en la validación de datos al crear eventos y mensajes de chat muy largos, incluyendo la posibilidad de introducir caracteres no válidos y la falta de indicaciones claras sobre los formatos esperados. 

  - Errata en Privacy Policy: Existe una errata en la política de privacidad. 

- **¿La aplicación respondió rápidamente a tus acciones?**  
Se ha obtenido para este apartado una puntuación media de 4.2.
- **En cuanto a estilos y diseño, ¿hay algo que no le gustase o que se pudiese cambiar?**
  - Diseño de Documentos: Se sugiere que los documentos grandes sean recortados. 

  - Validadores: Los errores de los formularios no se ven bien. 

  - Edición de profesional: El botón de borrar perfil está muy desentonado con el resto del HTML. 

- **¿Alguna recomendación de mejora?**
  - Mejorar las restricciones de los formularios: Algunos validadores pueden ser mejorados. 

  - Controlar las excepciones del servidor: Se puede implementar una pantalla de errores customizada para no alterar mucho la experiencia de usuario. 

  - Eliminar la opción de que los administradores puedan editar la contraseña de los usuarios normales. 

## Conclusión
  - Se han cumplido tres criterios de aceptación y uno ha obtenido una calificación intermedia. Se identifican áreas de mejora en usabilidad y funcionalidad. 

  - La aplicación recibió una calificación media de 4 en facilidad de uso. Se reportaron menos de 5 elementos confusos en la interfaz. Se identificaron 3 errores diferentes. La aplicación recibió una calificación media de 4.2 en velocidad de respuesta. 

  - Se señalaron áreas de mejora en diseño, varios usuarios pilotos pidieron mejorar los validadores, tanto backend como frontend. Además, se sugiere controlar excepciones del servidor. 





