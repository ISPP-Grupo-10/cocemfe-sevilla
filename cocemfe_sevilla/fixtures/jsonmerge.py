import json
import os

# Ruta de la carpeta fixtures
fixtures_dir = 'fixtures'

# Obtener la lista de archivos en la carpeta fixtures
files = os.listdir(fixtures_dir)

# Filtrar solo los archivos JSON que no sean sample_data.json
json_files = [os.path.join(fixtures_dir, file) for file in files if file.endswith('.json') and file != 'sample_data.json']

# Leer y combinar los datos de los archivos JSON
combined_data = []
for file in json_files:
    with open(file, encoding='utf-8') as f:  # Especificar la codificación como utf-8
        data = json.load(f)
        combined_data.extend(data)

# Escribir los datos combinados en un nuevo archivo JSON dentro de la carpeta fixtures
output_file = os.path.join(fixtures_dir, 'data.json')
with open(output_file, 'w', encoding='utf-8') as outfile:  # Especificar la codificación como utf-8
    json.dump(combined_data, outfile)

print("El archivo data.json ha sido sobrescrito con los datos combinados en la carpeta fixtures.")
