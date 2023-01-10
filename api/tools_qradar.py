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