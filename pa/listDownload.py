import requests

# List file list_href.txt
with open("list_href.txt", "r") as file:
    urls = [line.strip() for line in file.readlines()]


# Carpeta donde se guardarán los archivos descargados
output_folder = "downloads/"

# Asegúrate de que la carpeta exista
import os
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Descargar cada archivo
for i, url in enumerate(urls):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hubo algún error en la descarga

        # Nombre del archivo (puedes personalizarlo)
        filename = os.path.join(output_folder, f"file_{i + 1}.pdf")

        # Guardar el archivo
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Archivo descargado: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar {url}: {e}")