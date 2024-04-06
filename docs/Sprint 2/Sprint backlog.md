# Sprint backlog
****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 00/00/2024           | Sprint 2          |


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

****

## SPRINT BACKLOG

| ID | TAREA                        | DESCRIPCIÓN                                                   | PRIORIDAD | GRUPO |
|----|------------------------------|---------------------------------------------------------------|-----------|-------|
| 1  | Script populate              | Script para poblar la db con información de prueba           | Media     | 2     |
| 2  | Cambiar modelo documento: dates | Nuevos atributos para fechas: suggestion_start_date, suggestion_end_date, voting_start_date, voting_end_date | Muy alta | 2     |
| 3  | Cambiar modelo documento: status | -Estado Aportaciones: suggestion intérvalo -Estado Votaciones: review intérvalo -Estado En revisión: Tras votaciones -Estado Revisión: Tras review intérvalo | Muy Alta | 2     |
| 4  | Generar contraseña profesional | Cuando el admin crea un profesional, se genera automáticamente una contraseña | Alta      | 1     |
| 5  | Editar profesional            | Un profesional puede ver su perfil y editar el email, teléfono y establecer una nueva contraseña | Alta      | 1     |
| 6  | Inicio de sesión              | Inicio de sesión mediante email y contraseña                   | Muy alta  | 1     |
| 7  | Chat privado                  | Cada documento contará con un chat privado, accesible mediante un botón en detalles del documento, en el que solo podrán participar los revisores de dicho documento | Alta      | 3     |
| 8  | Chat privado – Admin          | El administrador tendrá acceso a todos los chats privados       | Alta      | 3     |
| 9  | Notificaciones documento      | Se enviará un email a todos los profesionales seleccionados como revisores | Media     | 2     |
| 10 | Notificaciones estado         | Se enviará un email a los revisores si un documento cambia de estado | Media     | 2     |
| 11 | Notificación bienvenida        | Se enviará un email al correo de un profesional cuando el admin lo registre en el sistema. El correo contiene las credenciales del profesional. | Media     | 2     |
| 12 | Notificación comentario        | Se enviará un email a todos los revisores cada vez que algún usuario escriba un comentario | Media     | 2     |
| 13 | Crear comentario              | En los detalles de un documento en aportaciones, un profesional podrá crear un comentario indicando concepto y relevancia. La fecha y el número de página de documento se registran automáticamente. | Alta      | 4     |
| 14 | Ver comentarios               | En los detalles de un documento en aportaciones, se listarán todos los comentarios realizados en dicho documento | Alta      | 4     |
| 15 | Navegación comentario         | Al hacer click en un comentario, se mostrará la página en la que se hizo | Alta      | 4     |
| 16 | Votaciones                    | Dado un comentario de un profesional, con el documento en estado de votaciones, otro podrá votar una única vez a favor o en contra de dicho comentario, dejando opcionalmente una justificación. La fecha y hora de la votación se registra automáticamente. | Alta      | 4     |
| 17 | Ver comentarios tras plazo    | En los detalles de un documento, el administrador podrá ver, tras el plazo de votaciones, un listado con los comentarios y sus votaciones (y votantes), claramente diferenciados aquellos con mayoría a favor. | Alta      | 4     |
| 18 | Subir documento modificado    | En los detalles de un documento, tras el plazo de aportaciones, el administrador podrá subir la nueva versión del documento y empezar el periodo de revisión. | Media     | 4     |
| 19 | Revisión final                | En los detalles de un documento en revisión, los revisores podrán dar su visto bueno (marcar como visto). | Media     | 4     |
| 20 | Listado visto bueno           | En los detalles de un documento en revisión, se listarán los revisores que han dado su visto bueno. | Media     | 4     |
