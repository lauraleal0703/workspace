import os
import json
from datetime import timedelta


def list_date(inicio, fin):
    lista_fechas = [str(inicio + timedelta(days=d)).split(" ")[0] for d in range((fin - inicio).days + 1)]
    return lista_fechas


def save_data_json(archivo, data, ruta, carpeta=None):
    if not os.path.exists(ruta):
        os.mkdir(ruta)
    if carpeta:
        carpetas = carpeta.split("/")
        if len(carpetas):
            for c in carpetas:
                ruta += f"{c}/"
                if not os.path.exists(ruta):
                    os.mkdir(ruta)

    nombre_archivo = f"{ruta}{archivo}.json"

    try:
        data_json = json.dumps(data)
        open(nombre_archivo, "w").write(data_json)

    except Exception as e:
        print(f"[error] save_data_json: {e}")