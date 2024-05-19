****
| NOMBRE DEL PROYECTO | CLIENTE  | EQUIPO DE TRABAJO | FECHA DE ELABORACIÓN | FASE DEL PROYECTO |
|---------------------|----------|-------------------|----------------------|-------------------|
| Cocemfe-Web         | COCEMFE  | Grupo 10          | 05/05/2024           | PPL               |


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

## REQUISITOS

- Python >= 3.7
- Django == 4.2.11

## PASOS

1. Clona el repositorio:
    ```bash
    git clone https://github.com/ISPP-Grupo-10/cocemfe-sevilla.git
    cd cocemfe_sevilla
    ```

2. Instala las dependencias:
    ```bash
    python -m pip install --upgrade pip
    pip install -r ./cocemfe_sevilla/requirements.txt
    pip install importlib_metadata
    ```

3. Realiza las migraciones a la base de datos:
    ```bash
    python ./cocemfe_sevilla/manage.py makemigrations
    python ./cocemfe_sevilla/manage.py migrate
    ```

4. Lanza el proyecto:
    ```bash
    python ./cocemfe_sevilla/manage.py runserver
    ```

## CONTRIBUCIONES

¡Aceptamos contribuciones! Para contribuir al proyecto, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea tu rama de funcionalidad usando el formato “feature/numeroIssue-nombre-rama":
    ```bash
    git checkout -b feature/issueNumber-branch-name
    ```

3. c.	Haz tus cambios y subelos al repositorio siguiendo la Conventional Commits convetion:
    ```bash
    git commit -m 'feat: add new feature'
    ```

4. Haz push al repositorio remoto:
    ```bash
    git push origin feature/issueNumber-branch-name
    ```

5. Haz una nueva pull request a la rama ‘develop’ y espera a ser aceptada.