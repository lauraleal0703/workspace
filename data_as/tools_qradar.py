import warnings
warnings.filterwarnings("ignore")

import requests
import logging
from datetime import datetime


######################################################
#------------Consumo de APIS de QRadar ---------------
######################################################


def curl_qradar(script: str, headers=None, params=None):
    """Función base para las llamadas a QRadar"""
    def_name = "curl_qradar"
    url_api = "https://172.16.17.10/api"
    try:
        r = requests.get(
            f"{url_api}/{script}",
            auth=("lleal", "wn4GQ*ndMHWKif"),
            verify=False,
            headers=headers,
            params=params)
        if r.status_code == 200:
            return r.json()
        return []
    except Exception as e:
        logging.error(f"{def_name}: {e}")
        return []


def offenses(headers=None, params=None):
    """siem"""
    return curl_qradar("siem/offenses", headers=headers, params=params)


def start_time_offenses(id_offense):
    def_name = "start_time_offenses"
    try:
        data_id_offense = offenses(
            params={
                "fields": "start_time",
                "filter": f"id={id_offense}"
            }
        )
        if data_id_offense:
            return int(data_id_offense[0]["start_time"])/1000
        else:
            return []
    except Exception as e:
        logging.error(f"{def_name}: {e}")
        return []
    

##################################
#------------Soporte--------------
###################################


def epoch2date_mili(epoch, formato="%Y-%m-%d %H:%M:%S"):
    """Convertir milisegundos a datetime
    formato="%Y-%m-%d %H:%M:&S" """
    def_name = "epoch2date"
    try:
        fecha = datetime.fromtimestamp(epoch/1000)

        return fecha.strftime(formato)

    except Exception as e:
        logging.error(f"{def_name}: {e}")
        return None

def epoch2date_seg(epoch, formato="%d/%m/%Y %H:%M:%S"):
    """Convertir milisegundos a datetime
    formato="%Y-%m-%d %H:%M:&S" """
    def_name = "epoch2date"
    try:
        fecha = datetime.fromtimestamp(epoch)

        return fecha.strftime(formato)

    except Exception as e:
        logging.error(f"{def_name}: {e}")
        return None

"""
data = tools_qradar.login_attempts(
        headers={"Range": "items=0-5"},
        params={
            "fields":"attempt_time",
            "filter": "attempt_result='SUCCESS'",
            "sort":"-attempt_time"
            }
        )

for pos, dato in enumerate(data):
    epoch = dato["attempt_time"]
    fecha_chl = tools_qradar.epoch2date(epoch)
    print(pos, fecha_chl)
"""