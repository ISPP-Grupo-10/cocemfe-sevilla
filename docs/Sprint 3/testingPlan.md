# Plan de Pruebas

****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 07/04/2024           | Sprint3           |


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

### PROPÓSITO DEL DOCUMENTO

Este documento describe el plan de pruebas para la aplicación de colaboración de documentos desarrollada para la ONG COCEMFE. El objetivo de este plan es garantizar la calidad y el correcto funcionamiento de la aplicación a través de una variedad de pruebas, incluyendo pruebas unitarias, de integración, End-to-End, de aceptación, exploratorias y de rendimiento.

****

### OBJETIVOS DE PRUEBAS
Los objetivos de las pruebas son los siguientes:
-	Verificar la funcionalidad y la calidad de la aplicación en diferentes niveles.
-	Identificar y corregir errores en la aplicación.
-	Evaluar el rendimiento y la usabilidad de la aplicación bajo diferentes condiciones.
-	Asegurar que la aplicación cumpla con los requisitos y expectativas del usuario final.

****

### ESTRATEGIA DE PRUEBAS
Los tipos de pruebas a realizar son las siguientes: 
Pruebas Unitarias
-	Se realizarán pruebas unitarias para validar el comportamiento individual de los componentes de código.
-	Se utilizará JUnit 5 como framework de pruebas unitarias.

Pruebas End-to-End
-	Se realizarán pruebas end-to-end para verificar el flujo completo de la aplicación desde el inicio hasta el final.  Estas pruebas se realizarán teniendo en cuenta su velocidad debido a que en ocasiones no merecen la pena debido a su lentitud a la hora de ejecutarlas en comparación al conjunto de tests y esto nos ería un obstáculo para progresar en los errores verdaderamente importantes.
-	Se utilizará Katalon Recorder junto con Selenium para automatizar las pruebas de extremo a extremo.

Pruebas de Aceptación
-	Se realizarán pruebas de aceptación basadas en escenarios Given-When-Then para validar que la aplicación cumple con los criterios de aceptación definidos por el cliente. Estas pruebas serán realizadas siempre y cuando les presentemos nuevas funcionalidades a la ONG en las reuniones semanales de aceptación.
-	Se utilizará Katalon Recorder junto con Selenium y JUnit 5 para escribir y ejecutar los casos de prueba de aceptación. En muchos casos, las pruebas End-to-End serán reutilizables debido a que nuestro cliente no está muy familiarizado con las tecnologías. Estas pruebas nos proporcionan un punto de vista visual y rápido, y dado que disponemos de poco tiempo en las reuniones, resultan especialmente útiles.

Pruebas Exploratorias
-	Se llevarán a cabo pruebas exploratorias para evaluar la usabilidad y la experiencia del usuario de la aplicación, priorizando la máxima simplicidad sobre el detalle.
-	Se realizarán sesiones de pruebas manuales con nuestros usuarios piloto para identificar problemas de usabilidad y sugerir mejoras.

Pruebas de Rendimiento 
-	Se realizarán pruebas de rendimiento para evaluar el rendimiento de la aplicación bajo diferentes condiciones de carga y para identificar posibles cuellos de botella.
-	Se utilizarán herramientas como Sonar o Gatling para realizar pruebas de carga y de estrés de forma incremental.

****

### PLAN DE EJECUCIÓN DE PRUEBAS
Asignación de Recursos
-	Los desarrolladores responsables de cada funcionalidad serán los encargados de realizar las pruebas respectivas. Se asignará de una a dos personas por tipo de test. En caso de no estar disponible, el desarrollador responsable, se designará un sustituto para llevar a cabo las pruebas.

Responsabilidades
-	Los desarrolladores de funcionalidades realizarán pruebas unitarias y de integración de las funcionalidades implementadas. También, comprobarán que las funcionalidades cumplen con los requisitos establecidos y funcionan correctamente. 

Comunicación y Seguimiento
-	Los desarrolladores informarán regularmente sobre el progreso de las pruebas al representante de cada grupo y se llevarán a cabo si es necesario una reunión breve para discutir cualquier problema encontrado durante las pruebas. Cualquier problema grave encontrado durante las pruebas será reportado inmediatamente al equipo de desarrollo para su resolución. Los resultados de las pruebas se documentarán y se compartirán con el equipo de desarrollo.

Seguimiento y Mejora Continua
-	Se realizará una evaluación posterior a la implementación de cada funcionalidad para identificar áreas de mejora en el proceso de pruebas. Además, en la retrospectiva se le dará una visión o tema particular al finalizar cada sprint para discutir lo aprendido y proponer mejoras para futuros.

****