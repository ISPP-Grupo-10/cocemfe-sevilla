# Gestión de la calidad

****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 16/02/2024           | Sprint1           |


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

## PROPÓSITO DE PROCESO DE MEJORA DE LA CALIDAD
Garantizar que el proyecto de desarrollo de software cumpla con los estándares de calidad establecidos y las
expectativas del cliente, asegurando que se entregue un producto final confiable y que cumple con los requisitos
especificados.

***

## PLANIFICACIÓN DE LA CALIDAD
La planificación de la calidad se llevará a cabo en una reunión de los responsables de cada grupo donde se detallará las herramientas y metodología para gestionar y controlar la calidad del código, documentación y la organización del desarrollo. Para lograr estos objetivos se usarán analizadores de código, estándares de codificación, revisiones a pares y realización de planes de testeo.

## ASEGURAMIENTO DE LA CALIDAD
En esta sección se detallará los procesos, herramientas y buenas prácticas a utilizar para asegurar la calidad del producto en los aspectos previamente descritos.

- **Calidad del código**: Para garantizar la calidad del código se empleará los estándares de códigos descritos en el documento de Metodlogías de trabajo y se utilizará el analizador de código Codacy como apoyo para garantizar la legibilidad y mantenimiento del código. Para el aseguramiento de la calidad de las funcionalidades del código se implementarán diversas pruebas unitarias sobre cada una de ellas y mediante el análisis de covertura de Codacy se observará la proporción de funcionalidades cubiertas por las pruebas. Para la ejecución de las pruebas se implementarán mediante el actions de Github un workflow para realizar integraciones continuas y agilizar la detección y resolución de posibles errores.

- **Calidad de la documentación**: Para asegurar la calidad de la presentación y contenido de los documentos se utilizarán plantillas predefinidas y se hará uso de herramientas de correción de ortografía de Word y el apoyo de inteligencias artificiales generativas como ChatGPT durante el desarrollo del documento. Adicionalmente todos los documentos pasaran por una revisión previa por una persona externa al grupo de creadores del mismo para asegurar la calidad del contenido y su entendimiento.

- **Calidad de la organización**: La calidad de organización en el desarrollo es vital para evitar pérdidas innecesarias de tiempo por esa razón llevaremos a cabo reuniones frecuentes con el cliente para asegurar la calidad de los requisitos establecidos asi como la satisfacción del mismo durante la evolución del producto. Otro aspecto de la organización en el desarrollo es la estructura y limpieza del repositorio para ello se implementarán plantillas de issues y conventional commits así como un tablero detallado para la gestión de tareas y la actualización del estado de las mismas.


## CONTROL DE LA CALIDAD
El control de la calidad se realizará primariamente mediante el analizador de código Codacy haciendo uso de sus métricas de calidad y cobertura para evaluar el estado del la calidad en el proyecto y se tomarán las acciones de mejoras proporcionadas por la herramienta. Para asegurar que el producto sigue los estándares de seguridad apropiados se realizarán auditorías de seguridad rutinarias y se contactará con un grupo diverso de usuarios pilotos con el objetivo de detectar posibles brechas de seguridad previas al despliegue oficial de la aplicación web.

Por último, se tendrá siempre en cuenta la aprobación del cliente en todo momento a la hora de implementar o modificar funcionalidades y la presentación de la aplicación web al cliente.

## MÉTRICAS DE CALIDAD 
| ID | Métrica                                           | Método de Medición                                                                                                                                                                                                            | 
|--------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **MI-001**      | Calidad de Código                  | Uso del analizador de código Codacy. | 
| **MI-002**      |  Cobertura de pruebas                  | Uso del analizador de cobertura Codacy. | 
| **MI-003**      | Aprobación del cliente                 | Encuestas o evaluaciones para medir la satisfacción del cliente con el producto o servicio entregado.                                                                                                                | 
| **MI-004**      | Cumplimiento de estándares de seguridad           | Auditorias de seguridad en las que se evalúa si el producto cumple con los estándares de seguridad establecidos y si se han corregido las vulnerabilidades identificadas.                                                                                         | 

## REFERENCIAS Y BIBLIOGRAFÍA
- https://chat.openai.com/share/8b7bacf5-4ea6-420f-bc26-2af01aff616f
- https://topodata.com/wp-content/uploads/2019/10/GUIA_PMBok.pdf