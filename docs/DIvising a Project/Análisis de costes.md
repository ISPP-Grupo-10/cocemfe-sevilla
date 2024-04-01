# Análisis de costes
****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 18/02/2024           | Sprint1           |


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

| **NIVEL DE EXACTITUD**  | **UNIDADES DE MEDIDA**  | **UMBRALES DE CONTROL**                                                                                                                                                                                                        |
|-------------------------|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Moneda: dos decimales   Tiempo: un decimal  | Moneda: euro   Tiempo: horas  | <p>Las horas de dedicación no pueden exceder en más de un  5% la planificación inicial.   </p><p>Los costes de mantenimiento están sujetos a las tarifas de las herramientas y las necesidades específicas del proyecto.  </p> |

****

## ÁMBITO DE APLICACIÓN Y CONTEXTO

La estimación de costes se hará en base al salario estimado y promedio de los puestos Junior de los distintos perfiles profesionales involucrados en el desarrollo de software.   

Somos  17  alumnos  del  Grado  de  ingeniería  del  software  en  la  asignatura  de  Ingeniería  del  Software  y  Práctica Profesional (ISPP), por lo que el salario del personal durante el presente desarrollo, en tanto tiempo imputado en concepto de práctica de dicha asignatura, se establece solo a título informativo y como práctica, no debiendo ser abonado por el cliente.

El coste de mantenimiento, por otra parte, es una estimación del coste que supondría a la organización seguir usando el producto una vez acabado el desarrollo y la asignatura. Dicho coste correrá a cargo de la organización siendo estos los responsables de contratar dado el caso, los servicios o personal oportunos. 

## PROPÓSITO DEL ANÁLISIS DE COSTES 

El análisis de costos es una práctica fundamental en la gestión empresarial que implica examinar y evaluar 
detalladamente todos los gastos asociados con la producción, operación y mantenimiento de un producto o servicio. 
Esta actividad proporciona información crucial para la toma de decisiones estratégicas y tácticas en un proyecto.  

****

## DESARROLLO DE LOS COSTES

### Costes de contratación de personal

| **Puestos/Roles**                          | **Tiempo de Trabajo**        | **Sueldo** | **Precio Mensual [1]** | **Precio Mensual Ponderado** | **Precio Total** |
|--------------------------------------------|------------------------------|------------|------------------------|------------------------------|------------------|
| Ingeniero de software Junior               | 150 horas                    | 20 €/h     | 3,000 €                 | 840 €/mes                    | 1,300 €          |
| **Total x17 personas**                    | **2,550 horas**              | **340 €/h**| **95,200 €/mes**        | **14,280 €/mes**             | **51,000 €**     |

### Recursos materiales[1] [2]

| Concepto                   | Precio       | Precio ponderado | Amortización del material |
|-----------------------------|--------------|------------------|---------------------------|
| Electricidad + agua        | 700 €/mes    | 105 €/mes        |                           |
| Oficina                    | 2700 €/mes   | 405 €/mes        |                           |
| Totales                    | 3895.83 €/mes| 584.38 €/mes     |                           |

### Costes de software de desarrollo[3]

| Concepto                 | Precio         |
|--------------------------|----------------|
| GitHub Team              | 68 €/mes       |
| OneDrive for Business    | 198.9 €/mes    |
| **Total**                | **266.9 €/mes**|

### Costes de mantenimiento [4]

| Concepto                  | Precio        |
|---------------------------|---------------|
| Coste de personal         | €/ 0.10 mes   |
| Google Cloud Platform     | 33.18 €/mes   |
| **Total**                 | **33.28 €/mes**|

### Costes de operación (OPEX) Estimado

| Concepto                     | Precio mensual ponderado | Descripción                                       |
|------------------------------|--------------------------|---------------------------------------------------|
| Costes de personal           | 14,280 €/mes             | Costo mensual promedio de 17 ingenieros de software junior. |
| Electricidad + Agua          | 105 €/mes                | Gasto mensual en electricidad y agua para la oficina. |
| Oficina                      | 405 €/mes                | Costo mensual de la amortización del espacio de oficina. |
| Herramientas de Desarrollo    | 68 €/mes                 | Suscripción mensual a GitHub Team.                  |
| Almacenamiento en la Nube     | 198.9 €/mes              | Suscripción mensual a OneDrive for Business.        |
| Mantenimiento del Software    | 33.28 €/mes              | Costo mensual del mantenimiento de MongoDB y Google Cloud Platform. |

### Costes de Capitalización (CAPEX)

| Concepto                  | Precio mensual ponderado | Descripción                                         |
|---------------------------|--------------------------|-----------------------------------------------------|
| Amortización del material | 74.38 €/mes              | Costo mensual de la amortización del material utilizado por cada desarrollador, ordenadores, monitores, etc. |

### Costes de Mantenimiento [4]

| Concepto                  | Precio        |
|---------------------------|---------------|
| Coste de personal         | €/ 0.10 mes   |
| Google Cloud Platform     | 33.18 €/mes   |
| **Total**                 | **33.28 €/mes**|

### Estimación TCO estimado (OPEX)

| Concepto               | Coste estimado | Coste real | Variación  |
|------------------------|----------------|------------|------------|
| Costes de personal     | 17,000 €       | 16,120 €   | 880 €      |
| Electricidad + Agua    | 122.5 €        | 122.5 €    | 0 €        |
| Oficina                | 472.5 €        | 472.5 €    | 0 €        |
| Herramientas de Desarrollo | 79.5 €     | 79.5 €     | 0 €        |
| Almacenamiento en la Nube  | 232.5 €   | 232.5 €   | 0 €        |
| Mantenimiento del Software  | 38.5 € | 38.5 €     | 0 €        |

### Estimación TCO estimado (CAPEX)

| Concepto                  | Coste estimado | Coste real | Variación  |
|---------------------------|----------------|------------|------------|
| Amortización del material | 86.5 €         | 86.5 €     | 0 €        |

## Totales y Resumen de Costes

- Coste mensual de operación: 14,280 + 584.38 + 266.9 + 33.28 = 15,164.56 €
- Coste total de operación: 3.57 * (584.38 + 266.9 + 33.28) + 51,000 = 54,157.79 €
- Coste de mantenimiento: 33.28 €

## Referencias y Justificación

1. Estimamos el mes promedio en 4.2 semanas. Consecuentemente, durante las 15 semanas de asignatura, consideramos para estimar los costes un total de meses de 3.57 meses aprox.
2. [Enlace a Idealista](https://www.idealista.com/inmueble/103842580/) → hemos extrapolado el coste de una oficina para 17 personas y lo hemos ponderado con las horas dedicadas comparada con una jornada laboral estándar (~40h/semana). Por tanto, se multiplica por 6/40 = 0.15; de este modo 2700 * 0.15 = 405, se ha procedido del mismo modo para el resto de los cálculos de costes fijos mensuales.
3. Costes software únicamente durante el desarrollo del proyecto.
4. Costes mensuales de mantenimiento del proyecto, estarán presente durante el desarrollo y a lo largo de la vida útil del producto. MongoDB tiene un coste de 0.10 € por millón de lectura, en este informe se presupone que la aplicación consume un millón de lecturas al mes. El coste se ha obtenido del documento "technology management".



