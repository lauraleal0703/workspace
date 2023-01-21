import os
import json
from datetime import timedelta


def list_date(inicio, fin):
    lista_fechas = [str(inicio + timedelta(days=d)).split(" ")[0] for d in range((fin - inicio).days + 1)]
    return lista_fechas


def save_data_json(archivo, data, carpeta=None):
    if carpeta:
        carpetas = str(carpeta).split("/")
        if len(carpetas):
            ruta = "data_collected/"
            if not os.path.exists(ruta):
                os.mkdir(ruta)
            for c in carpetas:
                ruta += f"{c}/"
                if not os.path.exists(ruta):
                    os.mkdir(ruta)
        else:
            if not os.path.exists(carpeta):
                os.mkdir(carpeta)

        carpeta = f"data_collected/{carpeta}"
        nombre_archivo = f"{carpeta}/{archivo}.json"

    else:
        nombre_archivo = f"data_collected/{archivo}.json"

    try:
        data_json = json.dumps(data)
        open(nombre_archivo, "w").write(data_json)

    except Exception as e:
        print(f"[error] guardar: {e}")