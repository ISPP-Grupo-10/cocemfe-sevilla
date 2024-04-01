# Guía de Revisión
****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 29/03/2024           | Sprint 2          |


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

## Pasos Previos

Este sistema permite a los usuarios la revisión colaborativa de planes de accesibilidad. Para ello, los profesionales pueden hacer aportaciones de cambio en los documentos a los que tienen acceso. Es el administrador el que crea los documentos y los profesionales. Sabemos que la pantalla principal de inicio está muy pobre, lo modificaremos para el siguiente sprint.

Dado que el estado de los documentos cambia según la fecha, para poder probar los distintos estados, se puede editar las fechas de inicio y fin de sugerencias y votación. Para que el estado sea ‘Borrador’, la fecha de inicio de sugerencias debe estar a futuro. Para que el estado sea ‘Aportaciones’, la fecha de inicio de sugerencias debe ser la fecha actual. Para que el estado sea ‘Votaciones’, la fecha de fin de sugerencias debe ser la actual (y la fecha de inicio de sugerencias se debe borrar).

## A Evaluar

Para todos los casos de uso, es necesario tener iniciada la sesión. Para ello, simplemente se accede al sistema y se introducen los datos (correo y contraseña).

![Login](../../static/images/cap_login.png)

## Caso de Uso: Subida de documento

1. **Login** como se indica anteriormente.
2. **Listado de documentos:** Aparecen todos los documentos a los que el usuario tiene acceso. El administrador tiene acceso a todos los documentos.
![Listar Documentos](../../static/images/cap_listar_docs.png)

3. **Subida de documentos introduciendo los datos:** En esta pantalla se puede subir un documento nuevo al sistema. Solo el administrador puede hacerlo. Dependiendo de las fechas que se introduzcan, el estado del documento será diferente. Si la fecha de inicio de aportaciones está en el futuro, el estado será ‘Borrador’. Cuando llegue esa fecha, cambiará a ‘Aportaciones’. Cuando llegue la fecha de cierre de aportaciones, se pasa al estado ‘Votaciones’. Una vez pase la fecha de Votaciones, pasa a ‘Revisión’.
![Subir Documento](../../static/images/cap_nuevo_doc.png)

### Caso de Uso: Modificar documentos

Para modificar documentos también se debe iniciar sesión y listar documentos. Después se pulsa en el botón de editar (el lápiz). El formulario de edición es el mismo que el de creación.

### Caso de Uso: Administrador registra profesionales

1. **Login** como se indica anteriormente.
2. **Listado de organizaciones**
![Listar Organizaciones](../../static/images/cap_listar_org.png)

3. **Crear organización**
![Crear Organización](../../static/images/cap_nueva_org.png)
4. **Listado de profesionales**
![Listar Profesionales](../../static/images/cap_listar_user.png)
5. **Registro del profesional introduciendo los datos**
![Registrar Profesional](../../static/images/cap_nuevo_user.png)

Cuando el administrador registra al profesional, este recibe un correo en el que obtiene una contraseña provisional generada. Con esta contraseña puede acceder al sistema.

### Caso de Uso: Visualización de pdf y aportaciones

Dependiendo del estado del documento se visualizará una cosa u otra. En caso de que esté en Borrador se verá el pdf y un contador hasta la fecha de inicio de las aportaciones:
![Visalizar documento en estado Borrador](../../static/images/cap_borrador.png)

En caso de que el estado sea Aportaciones, se podrán crear los comentarios. Para crearlos hay dos opciones:

- Se puede crear manualmente rellenando los campos uno a uno, donde ‘Cuerpo del comentario’ hace referencia a lo que se quiere aportar y ‘Sección’ es la parte del documento al que influye el comentario.
- También se puede capturar la selección de manera automática, seleccionando en el documento la parte a comentar y pulsando el botón de Capturar Selección. Cuando se haga esto, se rellena automáticamente la sección y el número de página. Cuando se cree el comentario, aparecerá en la parte derecha. Si se pulsa en él, se mostrará la página a la que hace referencia y se resaltará en amarillo la sección seleccionada.

![Visalizar documento en estado Aportaciones](../../static/images/cap_aportaciones.png)

En caso de que el estado sea ‘Votaciones’, se mostrará una pantalla parecida a la anterior, solo que ya no se podrán crear aportaciones y los comentarios tendrán un contador de aprobación/rechazo. Cada usuario (solo los profesionales) cuando pulsen en cada comentario podrán dar su voto a favor o en contra.
![Votar en sugerencia](../../static/images/cap_votar.png)

### Caso de Uso: Chat de equipo

Para cada documento hay un chat en el que los profesionales que tengan acceso al documento (incluido el administrador) podrán comunicarse entre sí. Para acceder, hay que pulsar el botón del chat que hay debajo de la vista de detalles del documento.
![Chat de equipo](../../static/images/cap_chat.png)

### Caso de Uso: Solicitud de registro

Si no eres usuario registrado en el sistema puedes mandar una solicitud de registro antes de hacer el login. Se pedirá el correo electrónico y una descripción de tus datos. De aquí el administrador obtendrá los datos del profesional para proceder al registro. 

Estas solicitudes son recibidas por el administrador.
![Listar solicitudes](../../static/images/cap_solicitudes.png)

Cuando el administrador ya haya revisado sus datos puede cambiar el estado de la solicitud.
![Revisar solicitud](../../static/images/cap_aceptar_solicitud.png)

## Datos necesarios

Proyecto desplegado: http://antoniomaqueda.pythonanywhere.com/
Credenciales del administrador: correo: ama@gmail.com / contraseña: ama
Credenciales de un profesional: correo: luis@pla.com / contraseña: ama
Landing Page: https://cocemfe-web-landing-page.vercel.app/
Clockify: https://app.clockify.me/shared/6606cc5e1e41eb36ffccaba0
GitHub: https://github.com/ISPP-Grupo-10/cocemfe-sevilla
Demo de la aplicación: https://github.com/ISPP-Grupo-10/cocemfe-sevilla/blob/main/docs/Sprint%202/demo.mp4





