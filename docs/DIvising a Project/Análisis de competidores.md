# Análisis de competidores
****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 16/02/2024           | Devising a project|


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

## PROPÓSITO DEL ANÁLISIS DE COMPETIDORES

El propósito de este documento es proporcionarnos una visión detallada de los competidores directos e indirectos, evaluando sus fortalezas, debilidades, estrategias y tácticas. Al identificar las distintas estrategias utilizadas por los competidores, podemos descubrir oportunidades para diferenciarnos y mitigar amenazas en el mercado.

Al realizar un análisis del panorama competitivo, este documento nos aportará la información necesaria para realizar tomas de decisión en función de las oportunidades y riesgos estudiados.

****

## ANÁLISIS DEL MERCADO

El enfoque principal de este apartado es identificar soluciones existentes que aborden problemas similares o que presenten funcionalidades relevantes para el proyecto que estás desarrollando. En este caso, buscar soluciones implementadas que permitan la subida de archivos en tiempo real y su edición colaborativa por múltiples usuarios sería una parte crucial del análisis del mercado.

### Aplicaciones Similares en el Mercado:

1. **Wheelmap:** Esta aplicación permite a los usuarios encontrar y compartir información sobre la accesibilidad de lugares y espacios públicos para personas con discapacidad. Aunque no aborda directamente la funcionalidad de subir y editar documentos en tiempo real, su enfoque en la accesibilidad podría ofrecer ideas sobre cómo presentar y compartir información relevante para personas con movilidad reducida.

2. **AccessibleGO:** AccessibleGO proporciona información sobre destinos accesibles y opciones de viaje para personas con discapacidad. Aunque se centra en viajes accesibles, su enfoque en la accesibilidad y la presentación de información podría inspirar la forma en que se presenta la información en nuestra aplicación.

3. **Dropbox Paper:** Dropbox Paper permite la colaboración en tiempo real en la edición de documentos. Su enfoque en la colaboración podría servir como referencia para la implementación de la funcionalidad de edición colaborativa de documentos en tu aplicación.

4. **Google Docs:** Google Docs es una herramienta popular que permite a los usuarios crear y editar documentos en tiempo real. Los usuarios pueden compartir documentos con otros y colaborar en su edición simultánea. Google Docs también proporciona funciones para agregar comentarios y realizar revisiones de documentos.

5. **Microsoft Office Online:** Microsoft Office Online es una versión en línea de la suite de Office que incluye Word, Excel, PowerPoint y otros programas. Permite a los usuarios crear y editar documentos en tiempo real a través de un navegador web. Los documentos pueden ser compartidos y colaborados con otros usuarios.

6. **Quip:** Quip es una aplicación de productividad que combina documentos, hojas de cálculo y listas de tareas en una sola plataforma colaborativa. Los usuarios pueden crear documentos y colaborar en su edición en tiempo real, así como comunicarse a través de chat integrado.

7. **Notion:** Notion es una aplicación todo en uno que permite a los usuarios crear documentos, bases de datos, tableros y otros elementos de contenido. Los usuarios pueden colaborar en la edición de documentos en tiempo real y organizar su trabajo de manera flexible.

### Funcionalidad de Subir Documentos en Tiempo Real y Edición Colaborativa:

Para implementar la funcionalidad de subir documentos en tiempo real y permitir su edición colaborativa en tu aplicación, se podría considerar las siguientes tecnologías y enfoques:

1. **Google Docs API:** La API de Google Docs permite integrar funcionalidades de Google Docs en tu aplicación, lo que permitiría a los usuarios crear, editar y colaborar en documentos en tiempo real.

2. **Microsoft Office Online API:** Similar a Google Docs API, la API de Microsoft Office Online permite la integración de funcionalidades de Office en tu aplicación, lo que facilitaría la colaboración en la edición de documentos de Word, Excel y PowerPoint en tiempo real.

3. **Amazon S3 (Simple Storage Service):** Amazon S3 es un servicio de almacenamiento en la nube altamente escalable y confiable. Puedes integrar Amazon S3 en tu aplicación para permitir que los usuarios suban y almacenen documentos en la nube de Amazon.

4. **Almacenamiento en la Base de Datos:** Puedes almacenar los documentos directamente en la base de datos de tu aplicación, utilizando un campo de tipo blob (objeto binario grande) para almacenar el contenido del documento. Sin embargo, este enfoque puede no ser ideal para documentos grandes o una gran cantidad de archivos debido a consideraciones de rendimiento y escalabilidad.

5. **WebSocket:** Puedes utilizar WebSocket para habilitar la comunicación bidireccional en tiempo real entre el cliente y el servidor. Esto permitirá actualizaciones instantáneas en la interfaz de usuario cuando se suban o modifiquen documentos.

6. **Firebase Realtime Database:** Firebase ofrece una base de datos en tiempo real que permite sincronizar datos en todos los clientes conectados en tiempo real. Puedes utilizar Firebase Realtime Database para almacenar los documentos y permitir la colaboración en tiempo real entre múltiples usuarios.

7. **WebRTC (Web Real-Time Communication):** WebRTC es una tecnología que permite la comunicación de voz, video y datos en tiempo real en aplicaciones web. Aunque está más orientada a la comunicación multimedia, también puede ser utilizada para la colaboración en documentos en tiempo real.

8. **ShareDB:** ShareDB es una base de datos en tiempo real para aplicaciones web. Permite la sincronización de datos en tiempo real entre clientes y servidores, lo que facilita la creación de aplicaciones colaborativas. Esta biblioteca está diseñada para trabajar con Node.js y MongoDB, pero también puede integrarse con otros sistemas de almacenamiento de datos. ShareDB ofrece una API simple y potente para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en datos compartidos entre múltiples clientes.

9. **TogetherJS:** TogetherJS es una biblioteca de código abierto que permite la colaboración en tiempo real en aplicaciones web. Con TogetherJS, los usuarios pueden ver las acciones de otros usuarios en tiempo real, como movimientos del cursor, selecciones de texto y cambios en el contenido de la página. La biblioteca proporciona herramientas para la colaboración en la edición de texto, formularios y otros elementos de la interfaz de usuario.

10. **Convergence:** Convergence es una plataforma de colaboración en tiempo real diseñada para aplicaciones web y móviles. Proporciona características avanzadas para la colaboración en la edición de documentos, como la detección de conflictos, la sincronización automática de cambios y el historial de revisiones. Convergence ofrece una API flexible y extensible que permite integrar fácilmente la funcionalidad de colaboración en cualquier aplicación web o móvil.

## CONCLUSIÓN

El análisis del mercado revela que en el mercado existen varias alternativas a una aplicación en la cual se puedan subir documentos en tiempo real, que estos se guarden para que otros usuarios puedan consultarlos y modificarlos.

Aunque estas aplicaciones no están orientadas a nuestro público objetivo que sería aquellos técnicos especialistas (arquitectos, aparejadores, etc.) que puedan consultar, modificar y aprobar estos documentos específicos para la construcción de distintos proyectos con la finalidad de ayudar a estas personas con movilidad reducida en distintas áreas incapaz de acceder. Es aquí donde podremos hacer uso de las distintas tecnologías para la subida de documentos, almacenamiento de estos y modificación, consulta por los técnicos especialistas en tiempo real.

## REFERENCIAS Y BIBLIOGRAFÍA

- [Wheelmap](https://wheelmap.org/?locale=es)
- [AccessibleGO](https://accessiblego.com/)
- [Chat OpenAI](https://chat.openai.com/share/851f58cb-1c8c-42d8-bfca-bed1fffdd9dc)

