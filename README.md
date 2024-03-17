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

## Contribución

¡Agradecemos contribuciones! Para contribuir al proyecto, sigue estos pasos:
1. Forkea el proyecto.
2. Crea tu rama de características usando el formato `feature/numeroissue-nombre-de-la-rama`:
```bash
git checkout -b feature/numeroissue-nombre-de-la-rama
```
Por ejemplo:
```bash
git checkout -b feature/123-nueva-caracteristica
```
3.Realiza tus cambios y haz commit de ellos siguiendo las convenciones de Conventional Commits:
```bash
git commit -m 'feat: agregar nueva característica'
```
4. Haz push a tu repositorio remoto:
```bash
git push origin feature/numeroissue-nombre-de-la-rama
```
5. Realiza una pull request a Develop y espera a que sea aceptada :)
