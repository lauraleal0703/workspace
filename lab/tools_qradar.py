import warnings
warnings.filterwarnings("ignore")

import requests
import logging
from datetime import datetime


##########################################
#------------Consumo de APIs--------------
##########################################


def curl_general(script: str, headers=None, params=None):
    """Función base para las llamadas"""
    def_name = "curl_general"
    try:
        r = requests.get(
            script,
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


def login_attempts(headers=None, params=None):
    """access"""
    return curl_qradar("access/login_attempts", headers=headers, params=params)


def ariel_searches(headers=None, params=None):
    """ariel"""
    return curl_qradar("ariel/searches", headers=headers, params=params)


def rules(headers=None, params=None):
    """analytics"""
    return curl_qradar("analytics/rules", headers=headers, params=params)


def domain_management_domains(headers=None, params=None):
    """config"""
    return curl_qradar("config/domain_management/domains", headers=headers, params=params)


def offenses(headers=None, params=None):
    """siem"""
    return curl_qradar("siem/offenses", headers=headers, params=params)


def offense_types(headers=None, params=None):
    """siem"""
    return curl_qradar("siem/offense_types", headers=headers, params=params)

#################################
#------------Ejemplos-----------
################################

# data_2 = tools_qradar.domain_management_domains(headers={"Range": "items=0-1"})
# data_3 = tools_qradar.offense_types(headers={"Range": "items=0-1"})
# data_4 = tools_qradar.ariel_searches(headers={"Range": "items=0-1"})

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


##################################
#------------Soporte--------------
###################################


def epoch2date(epoch, formato="%d/%m/%Y %H:%M:%S"):
    """Convertir milisegundos a datetime
    formato="%Y-%m-%d %H:%M:&S" """
    def_name = "epoch2date"
    try:
        fecha = datetime.fromtimestamp(epoch/1000)

        return fecha.strftime(formato)

    except Exception as e:
        logging.error(f"{def_name}: {e}")
        return None