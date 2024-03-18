import os
import django
import sys
import json
from django.contrib.auth.hashers import make_password

# Obtener la ruta al directorio del proyecto Django
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agregar el directorio del proyecto al PYTHONPATH
sys.path.append(project_dir)

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocemfe_sevilla.settings')
django.setup()

# Ruta de la carpeta fixtures
fixtures_dir = 'fixtures'

# Obtener la lista de archivos en la carpeta fixtures
files = os.listdir(fixtures_dir)

# Filtrar solo los archivos JSON que no sean sample_data.json
json_files = [os.path.join(fixtures_dir, file) for file in files if file.endswith('.json') and file != 'data.json']

# Leer y combinar los datos de los archivos JSON
combined_data = []
for file in json_files:
    with open(file, encoding='utf-8') as f:  # Especificar la codificación como utf-8
        data = json.load(f)
        # Verificar si el archivo es de usuarios (professionals u organizations)
        for entry in data:
            fields = entry.get('fields', {})  # Obtener los campos de la entrada
            password = fields.get('password')  # Obtener la contraseña si existe
            if password:  # Verificar si la contraseña existe
                # Cifrar la contraseña antes de combinar los datos
                fields['password'] = make_password(password)
        combined_data.extend(data)

# Escribir los datos combinados en un nuevo archivo JSON dentro de la carpeta fixtures
output_file = os.path.join(fixtures_dir, 'data.json')
with open(output_file, 'w', encoding='utf-8') as outfile:  # Especificar la codificación como utf-8
    json.dump(combined_data, outfile)

print("El archivo data.json ha sido sobrescrito con los datos combinados en la carpeta fixtures.")
