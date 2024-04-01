# Análisis preliminar de riesgos

****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 18/02/2024           | Devise a Project  |


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

## ANÁLISIS DE RIESGOS

| Factor                             | Probabilidad                          |
|------------------------------------|---------------------------------------|
| Media (Impactos) * Probabilidad    | **Alta** = 3, **Media** = 2, **Baja** = 1 |



| ID  | CATEGORÍA      | RIESGO                                           | PRIORIDAD | IMPACTO ALCANCE | IMPACTO TIEMPO | IMPACTO COSTE | PROBABILIDAD | FACTOR | INTERESADO        | RESPONSABLE              | RESPUESTA / PLAN CONTINGENCIA                                                                                                                                                                                                                                                                                    |
|-----|----------------|--------------------------------------------------|-----------|-----------------|----------------|---------------|--------------|--------|-------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Organizacional | Falta de respuesta de la ONG                     | Alta      | -               | Alto           | -             | Alta         | 3      | Cliente           | Representante subgrupo 1 | Involucración activa del cliente en el desarrollo y constantes comunicaciones. Reuniones presenciales en caso de no respuesta por medios digitales.                                                                                                                                                              |
| 2   | Requisitos     | Cambios en los requisitos                        | Alta      | Alto            | Medio          | Medio         | Alta         | 6      | Cliente           | Equipo de trabajo        | Se evaluará el impacto de los cambios y se decidirá si alterar el Sprint Backlog actual o si se incluirá en uno siguiente.                                                                                                                                                                                       |
| 3   | Mantenimiento  | Cambio de plataforma de despliegue               | Baja      | Medio           | Medio          | Bajo          | Baja         | 2      | Cliente           | Equipo de trabajo        | Evaluación del impacto en las 3 dimensiones y se evaluará si incluirlo en este Sprint o en el siguiente.                                                                                                                                                                                                          |
| 4   | Organizacional | Baja de personal                                 | Media     | -               | Medio          | Bajo          | Baja         | 1      | Equipo de trabajo | Equipo de trabajo        | La carga de trabajo del personal ausente se reparte entre otros miembros del equipo en una reunión. Para evitar el Bus Factor, todos los integrantes dentro de cada subgrupo deberán tener capacidades y conocimientos similares y se formará a aquellos que les falten dichos conocimientos dentro de su subgrupo. |
| 5   | Organizacional | Problemas de capacitación del personal de la ONG | Baja      | -               | Bajo           | Bajo          | Baja         | 1      | Cliente           | Representante subgrupo 1 | Envío de personal del equipo para reforzar el uso y entendimiento de la herramienta.                                                                                                                                                                                                                             |
| 6   | Estimación     | Fallo de estimación de un requisito              | Media     | -               | Medio          | Bajo          | Media        | 2      | Equipo de trabajo | Equipo de trabajo        | Se reestima el requisito y se decide qué hacer con la tarea dependiendo del resultado.                                                                                                                                                                                                                           |
| 7   | Técnico        | Insuficiente cobertura de las pruebas            | Baja      | -               | Bajo           | Bajo          | Baja         | 1      | Equipo de trabajo | Representante subgrupo 4 | Se realizará un análisis de las líneas de código y casos de uso cubiertos por las pruebas actualmente y se realizará un nuevo plan de pruebas.                                                                                                                                                                 |
