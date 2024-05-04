FROM python:3.10-slim

# Configurar entorno de producción
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1


# Instalar dependencias
RUN apt-get update && apt-get install -y --no-install-recommends \
    git libpq-dev gcc libc-dev gcc g++ make libffi-dev python3-dev build-essential rsync sqlite3 libsqlite3-dev && \
    apt-get clean

COPY cocemfe_sevilla/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone --branch develop https://github.com/ISPP-Grupo-10/cocemfe-sevilla.git /app

WORKDIR /app/cocemfe_sevilla

RUN python manage.py makemigrations --noinput
RUN python manage.py migrate
RUN python manage.py loaddata fixtures/data.json


EXPOSE 8000
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
