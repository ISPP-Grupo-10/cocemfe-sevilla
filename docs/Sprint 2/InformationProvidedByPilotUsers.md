# Análisis de costes
****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 31/03/2024           | Sprint 2          |


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

- **#1.** Ante la pregunta “¿Encontraste la aplicación fácil de usar?”, obtener una puntuación media entre 4 y 5. Fracaso es considerado entre 1 y 2. El resto de puntuación sería una valoración intermedia.
- **#2.** Ante la pregunta “¿Hubo algún elemento de la interfaz que te resultara confuso o difícil de entender?”, obtener menos de 5 incidencias diferentes.
- **#3.** Ante la pregunta “¿Has encontrado algún fallo?”, obtener 3 o menos errores diferentes.
- **#4.** Ante la pregunta “¿La aplicación respondió rápidamente a tus acciones?”, el criterio es el mismo que en la pregunta #1.
- **#5.** Ante la pregunta “En cuanto a estilos y diseño, ¿hay algo que no le gustase o que se pudiese cambiar?”, no hay resultados objetivo, simplemente es para tener en cuenta la opinión para plantear posibles mejoras.
- **#6.** Ante la pregunta “¿Alguna recomendación de mejora?”, no hay resultados objetivo, simplemente es para tener en cuenta la opinión para plantear posibles mejoras.

**Criterio** | **#1** | **#2** | **#3** | **#4** | **#5** | **#6**
--- | --- | --- | --- | --- | --- | ---
**Alcanzado** | No | No | No | Sí | N/A | N/A

## Análisis de criterios de aceptación establecidos
- **¿Encontraste la aplicación fácil de usar?**  
Se ha obtenido una puntuación media de 3.6.
- **¿Hubo algún elemento de la interfaz que te resultara confuso o difícil de entender?**
  - Inicio de Sesión: Sugieren una mejor orientación al usuario en los enlaces al "Customer Terms" al iniciar sesión para una comprensión más clara de la página de inicio.
  - Sección de Profesionales: Confusión respecto a la utilidad de los filtros en la sección "Profesionales", ya que no se muestra contenido tras aplicarlos.
  - Creación de Organizaciones: El mensaje de error relacionado con el código postal al crear una nueva organización se considera poco informativo. Se sugiere proporcionar una guía más clara sobre el formato adecuado del código postal.
  - Guía de Uso: Falta de explicación clara sobre la función del botón "¿No tienes cuenta?" en la guía de uso.
  - Navegación y Modificación de Solicitudes: Dificultad para acceder a la pantalla de "Detalles de Sugerencias" y para modificar una solicitud debido a la falta de indicadores visuales.
  - Sección de Organizaciones: Recomendación de modificar el mensaje de error relacionado con el código postal para ofrecer una descripción más precisa del problema.
- **¿Has encontrado algún fallo?**
  - Funcionalidad General: Se ha observado la capacidad de crear documentos sin asociar profesionales, lo cual puede generar inconsistencias en la base de datos. Se reporta un mensaje de error relacionado con la política de origen cruzado y la sintaxis de metadatos, lo que indica problemas potenciales de seguridad y formateo en la respuesta del servidor.
  - Navegación y Funcionalidades Específicas: Existe la percepción de que el botón de "Perfil" no redirige correctamente al perfil del usuario, lo que puede deberse a un fallo de implementación o falta de funcionalidad. Se han registrado errores al acceder a la sección de documentos, con mensajes relacionados con la política de origen cruzado, lo que sugiere problemas de comunicación entre el cliente y el servidor.
  - Formularios y Campos de Texto: Se ha identificado la posibilidad de escribir textos demasiado largos en diversos campos, lo que causa problemas de visualización y puede afectar la usabilidad. Los campos de número de teléfono no validan correctamente las entradas, lo que puede resultar en datos incorrectos o incompletos sin una indicación clara para el usuario.
  - Registro y Creación de Solicitudes: Se ha detectado la capacidad de generar solicitudes de gran tamaño, lo que puede sobrecargar la aplicación y afectar su rendimiento. La falta de restricciones en la longitud de los campos de texto en el chat puede provocar interrupciones en la experiencia del usuario al escribir mensajes.
  - Edición y Validación de Datos: Se han identificado errores en la validación de datos al crear profesionales, documentos y organizaciones, incluyendo la posibilidad de introducir caracteres no válidos y la falta de indicaciones claras sobre los formatos esperados.
- **¿La aplicación respondió rápidamente a tus acciones?**  
Se ha obtenido para este apartado una puntuación media de 4.4.
- **En cuanto a estilos y diseño, ¿hay algo que no le gustase o que se pudiese cambiar?**
  - Interfaz General: Se ha destacado la percepción de pobreza en el diseño en varias pantallas, sugiriendo trabajar en la mejora visual en futuros sprints para lograr una apariencia más atractiva y coherente en toda la aplicación. Se sugiere mejorar visualmente el chat, destacando los mensajes propios sobre los demás y optimizando el uso del espacio en pantalla para una mejor legibilidad y experiencia de usuario.
  - Página de Inicio: Se elogia la apariencia de la landing page, pero se señala la presencia de texto de ejemplo y enlaces rotos que deben corregirse para una presentación más profesional y funcional. Se sugiere agregar contenido más atractivo en la página principal, como información sobre la organización, antes de presentar los enlaces, para captar la atención del usuario de manera más efectiva.
  - Listado de Profesionales: Se observa confusión en la ubicación de los filtros, ya que el cuadro de selección está situado en una posición diferente a la de los filtros. Se sugiere mejorar la claridad visual en esta área.
  - Navegación y Traducción: Se reportan problemas de navegación desde el correo electrónico de un usuario específico y errores de traducción ("spaninglish"), que pueden afectar la experiencia del usuario y deben corregirse para una comunicación más clara y coherente.
  - Diseño de Documentos: Se sugiere mejorar la visualización de comentarios y votos en la sección de detalles de los documentos, así como centrar el cuadro de comentarios y el botón de enviar mensaje para una mejor disposición en pantalla. También se propone mostrar el voto del usuario en los detalles de la sugerencia si ya ha votado, en lugar de presentarlo como vacío.
  - Mejoras Generales: Se recomienda resaltar los errores de los formularios en rojo para una identificación más clara y rápida por parte del usuario. Además, se sugiere truncar los campos de texto largos para evitar que la página se desborde hacia la derecha, mejorando así la legibilidad y la estética general.
- **¿Alguna recomendación de mejora?**
  - Edición de Documentos: Implementar una funcionalidad que permita editar documentos sin necesidad de volver a cargar el archivo original, lo que agilizaría el proceso de edición y evitaría la pérdida de datos.
  - Idioma y Realismo de Datos: Revisar y traducir completamente la interfaz al español para una experiencia más coherente y accesible para todos los usuarios. Implementar validaciones más estrictas en los campos de entrada, como números de teléfono y números de licencia, para garantizar datos más realistas y útiles en la base de datos.
  - Diseño Visual: Continuar mejorando la estética general de la aplicación, prestando especial atención a evitar campos de texto infinitos y asegurando una experiencia de usuario visualmente atractiva y funcional. Mejorar la apariencia y funcionalidad del chat, considerando la posibilidad de añadir notificaciones de nuevos mensajes en la barra del menú para una mejor visibilidad y accesibilidad.
  - Gestión de Solicitudes: Incluir un checkbox en las solicitudes para aceptar los términos del Acuerdo de Cliente y la Política de Privacidad, con la opción de traducir el Customer Agreement para facilitar la comprensión de usuarios no angloparlantes. Implementar mensajes de confirmación después de modificar o crear documentos, organizaciones u otras entidades, para proporcionar retroalimentación inmediata al usuario sobre el éxito de sus acciones.
  - Filtrado y Gestión de Contenidos: Agregar opciones de filtrado por estado de solicitud en la pantalla de Solicitudes para facilitar la búsqueda y gestión de solicitudes pendientes o en proceso. Incluir un aviso de confirmación antes de eliminar documentos u otros elementos importantes para prevenir errores accidentales y la pérdida de datos.
  - Funcionalidad Adicional: Explorar la posibilidad de permitir votaciones desde los comentarios en la sección de documentos, lo que facilitaría la participación y la interacción de los usuarios en la plataforma.


## Conclusión
- Se han superado los criterios de aceptación de una de las preguntas, y otra con un intervalo intermedio, con algunas áreas de mejora en la usabilidad y funcionalidad.
- Se destaca la necesidad de mejorar la claridad en la interfaz, especialmente en áreas como el inicio de sesión, la navegación y la visualización de documentos.
- Se sugiere una revisión exhaustiva del diseño y la estética de la aplicación, incluyendo la traducción completa al español y la implementación de validaciones más estrictas en los campos de entrada.
- Las recomendaciones de mejora incluyen la optimización de la experiencia del usuario en la edición de documentos, la gestión de solicitudes y la inclusión de funcionalidades adicionales, como la capacidad de votar desde los comentarios.




