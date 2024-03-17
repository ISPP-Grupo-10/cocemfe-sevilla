# Cocemfe Web

Cocemfe Web es un proyecto elaborado por 17 estudiantes de ingeniería del software que pretende mejorar la eficiencia de todos los municipios a la hora de crear planes de accesibilidad. El software permite la subida de documentos para que, posteriormente, una serie de personas cualificadas puedan sugerir mejoras al documento, haciendo así el proceso de edición del plan y propuesta de mejoras mucho más ameno.

## Instalación

### Requisitos

- Python >= 3.7

### Pasos

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/cocemfe-web.git
cd cocemfe-web
```
2. Instala las dependencias:

```bash
python -m pip install --upgrade pip
pip install -r ./cocemfe_sevilla/requirements.txt
pip install importlib_metadata
```
3. Realiza las migraciones de la base de datos:

```bash
python ./cocemfe_sevilla/manage.py makemigrations
python ./cocemfe_sevilla/manage.py migrate
```
4. Lanza el proyecto

```bash
python ./cocemfe_sevilla/manage.py runserver
```
