# Manual Usuario
****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 22/04/2024           | PPL               |


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

## 1. INTRODUCCIÓN

El presente documento es un manual para aprender a utilizar la aplicación COCEMFE WEB. Esta aplicación consiste en un gestor de documentos colaborativo, centrado en la creación y desarrollo de planes de accesibilidad. Gracias a este software, se podrán redactar estos planes de forma sencilla y rápida.

En este manual encontrarás una guía inicial con la que adquirir los conocimientos necesarios para el manejo de esta aplicación.


## 2. ROLES

En primer lugar, debemos conocer que hay dos roles distintos con funcionalidades distintas:

-	Administrador: Es el encargado de publicar los planes, registrar a los profesionales y organizaciones, y de crear eventos. Podrá acceder a todos los documentos, sugerencias y votaciones, además de al mapa de localizaciones. Solo hay uno (mientras no se diga lo contrario)
-	Profesionales: Son todos los demás usuarios. Se encargar de leer, revisar, aportar y valorar los documentos a los que son asignados. 


## 3. FUNCIONALIDADES

### 3.1 Registro

Solo el administrador es capaz de registrar profesionales, por lo que no cualquier persona puede acceder al sistema. Para ello, es necesario indicar los datos del profesional y de la organización a la que pertenece.
Cuando se registre al profesional, recibirá un correo electrónico, que le proporcionará una contraseña provisional. Tendrá que activar su cuenta mediante el enlace que recibe y cambiará su contraseña. 

![Nueva Organizacion](../../static/images/cap_nueva_org.png)

![Nuevo Documento](../../static/images/cap_nuevo_user.png)

Por otro lado, para facilitar el registro a los administradores, aunque un usuario cualquiera no puede registrarse por si mismo en el sistema, sí que puede enviar una solicitud, mediante la que el administrador podrá obtener sus datos. Para ello, en la pantalla de registra se pulsa “¿No tienes una cuenta?”

#### 3.1.1 Cambio de constaseña
En la pantalla de inicio de sesión, encontrarás un botón “¿Has olvidado tu contraseña?” que te llevará a la siguiente pantalla:

![Contraseña olvidada](../../static/images/cap_contra_olv.png)

Tras introducir el correo electrónico te llegará un mensaje con el enlace mediante el cual podrás acceder al cambio de contraseña:

![Cambio contraseña](../../static/images/cap_cambio_contra.png)
### 3.2 Documentos
Como hemos mencionado antes, solo los administradores pueden publicar documentos. Los documentos solo podrán ser en formato pdf. Para ello, introducirán los datos del documento:

![Subir Documento](../../static/images/cap_nuevo_doc.png)

En este proceso, se definirán las fechas de inicio y fin de las aportaciones, y el inicio y fin de las votaciones. También, se decide qué profesionales son los que tendrán acceso a ese documento.
Cuando se sube el documento, se envía un correo notificación a los profesionales seleccionados.
Dependiendo de las fechas que se introduzcan, el estado del documento será diferente. Si la fecha de inicio de aportaciones está en el futuro, el estado será ‘Borrador’. Cuando llegue esa fecha, cambiará a ‘Aportaciones’. Cuando llegue la fecha de cierre de aportaciones, se pasa al estado ‘Votaciones’. Una vez pase la fecha de Votaciones, pasa a ‘Revisión’

![Visalizar documento en estado Borrador](../../static/images/cap_borrador.png)

En caso de que el estado sea Aportaciones, se podrán crear los comentarios. Para crearlos hay dos opciones:

- Se puede crear manualmente rellenando los campos uno a uno, donde ‘Cuerpo del comentario’ hace referencia a lo que se quiere aportar y ‘Sección’ es la parte del documento al que influye el comentario.
- También se puede capturar la selección de manera automática, seleccionando en el documento la parte a comentar y pulsando el botón de Capturar Selección. Cuando se haga esto, se rellena automáticamente la sección y el número de página. Cuando se cree el comentario, aparecerá en la parte derecha. Si se pulsa en él, se mostrará la página a la que hace referencia y se resaltará en amarillo la sección seleccionada.

![Visalizar documento en estado Aportaciones](../../static/images/cap_aportaciones.png)

En caso de que el estado sea ‘Votaciones’, se mostrará una pantalla parecida a la anterior, solo que ya no se podrán crear aportaciones y los comentarios tendrán un contador de aprobación/rechazo. Cada usuario (solo los profesionales) cuando pulsen en cada comentario podrán dar su voto a favor o en contra.
![Votar en sugerencia](../../static/images/cap_votar.png)



### 3.3 Eventos

Cuando se crea el documento, se crean eventos con las fechas de inicio y fin de aportaciones y votaciones, las cuales se muestran en el calendario. Cada usuario ve en su calendario, los eventos en los que participa. El administrador ve todos los eventos:
![Calendario](../../static/images/cap_calendario.png)

Además, el administrador puede crear un evento independiente. Normalmente enfocado a reuniones:

![Crear Evento](../../static/images/cap_crear_evento.png)

### 3.4 Mapa

El administrador tiene a su disposición un mapa que marca todos los municipios y localidades que tienen un plan de accesibilidad. De esta forma, es fácil registrar cuales son los municipios a los que les falta:

![Mapa](../../static/images/cap_mapa.png)

### 3.5 Perfil

En la parte superior derecha vemos un botón de ‘Perfil’. Accediendo a él se puede editar el perfil del usuario, además de cambiar la contraseña o eliminar la cuenta:

![Perfil](../../static/images/cap_perfil.png)


### 3.6 Donaciones

Cualquier usuario, sea profesional o no, puede hacer una donación a la ONG. Accediendo al botón de ‘Donar’ que se encuentra en la pantalla de inicio de sesión, a la que puede acceder todo el mundo, se puede realizar la transferencia mediante PayPal:

![Donaciones](../../static/images/cap_donaciones.png)

## 4. PROBLEMAS Y DUDAS FRECUENTES

- **He subido un pdf y está en estado de aportaciones, pero cuando intento seleccionar un apartado del documento, no se subraya. ¿Qué hago?**
Esto puede ser porque el pdf no sea legible. Eso no significa que no se pueda leer, sino que no es interpretable por la máquina, por lo que no consigue encontrar texto para subrayar. Tiene fácil solución: sube el pdf a esta página y transfórmalo en texto legible, el documento resultante sí podrá ser subrayado por la aplicación: https://www.pdf2go.com/es/convertir-a-pdf

- **El administrador ya me ha registrado como profesional, pero no consigo acceder al sistema con mi correo.**
Es probable que no hayas activado la cuenta todavía. Cuando el administrador te de de alta en el sistema, te llegará un correo de activación de la cuenta. En este correo hay un enlace, que te llevará a activar la cuenta. Una vez hecho esto, podrás usar tu cuenta sin problemas.
- **La contraseña provisional que se me ofrece en el correo no me funciona. ¿Cómo accedo a la aplicación?**
Si la contraseña provisional no te funciona prueba a cambiar la contraseña por una propia. De esta forma, podrás solucionar este problema y acceder a la aplicación.
- **Quiero probar a subir un documento en estado de Aportaciones directamente, pero no quiero tener que esperar a que llegue el día de las aportaciones. ¿Cómo puedo cambiarle el estado al documento?**
No puedes cambiarle el estado al documento como tal, pero sí puedes editar la fecha de aportaciones. Para ello, asigna la fecha de inicio de aportaciones a la fecha actual. De esta forma, el estado del documento será de Aportaciones. Para que sea de votaciones, asigna la fecha de fin de aportaciones a la fecha actual. Lo mismo con el estado de revisión, asigna la fecha de fin de votaciones a la fecha actual. Debes tener en cuenta que las fechas anteriores no deben estar asignadas, por lo que debes dejarlas en blanco.


## 5. SOPORTE Y CONTACTO

Para cualquier consulta o sugerencia, no dude ponerse en contacto con nosotros enviándonos un email a: cocemfesevillanotificaciones@gmail.com





