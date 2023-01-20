import db
import tools_data
import tools_qradar

from models import Ticket
from pprint import pprint
from datetime import datetime, timedelta

import os
import re
import numpy as np

# frase = "criticidad es baja"
# buscar =  re.findall(r"criticidad|baja", frase)
# print(len(buscar), buscar)



# print(">>---------Prueba personalizada---------------")

# data_otrs = db.session.query(Ticket).filter(Ticket.tn == 2022120154001332).first()
# # data_otrs = db.session.query(Ticket).filter(Ticket.title.like("61817%")).all()
# print(data_otrs.title)
# print(set(re.findall(r"\d{5,}|-|\d{5,}", data_otrs.title)))
# print(len(re.findall(r"\d{5,}|-|\d{5,}", data_otrs.title)))
# exit()

# print(data_otrs.title)
# print(data_otrs.create_time)

# data_qradar = tools_qradar.offenses(
#                 params={
#                     "fields": "start_time",
#                     "filter": f"id=61817"
#                     }
#                 )
# epoch = data_qradar[0]["start_time"]
# fecha_chl = tools_qradar.epoch2date_mili(epoch)
# print(fecha_chl)


# inicio = datetime(2012,1,1)
# fin   = datetime(2012,12,31)
# lista_fechas = [str(inicio + timedelta(days=d)).split(" ")[0] for d in range((fin - inicio).days + 1)] 
# print(lista_fechas)

# year = 2022
# # Definir el periodo que se quiere consultar
# list_date = tools_data.list_date(datetime(year,1,1), datetime(year,12,31))

#     print(fecha)
#     print(type(fecha.split("-")[0]))

# for type_case in tools_data.types_cases():
#     new_dictionary = f"dict_ticket_{type_case}"
#     new_dictionary = {}

ticket_offenses_year = {}
year = 2022
list_date = tools_data.list_date(datetime(year,1,30), datetime(year,2,4))

for date in list_date:
    inicio_date = datetime.now()

    if date.split("-")[1] not in ticket_offenses_year:
        ticket_offenses_year[date.split("-")[1]] = {}

    if date.split("-")[2] not in ticket_offenses_year[date.split("-")[1]]:
        ticket_offenses_year[date.split("-")[1]][date.split("-")[2]] = {
            "handwork": {
                "success": {
                    "low": {},
                    "mean": {},
                    "high": {}
                    },
                    "fails": {
                        "low": {},
                        "mean": {},
                        "high": {}
                        }
            },
            "automatic": {
                "success": {
                    "low": {},
                    "mean": {},
                    "high": {}
                    },
                    "fails": {
                        "low": {},
                        "mean": {},
                        "high": {}
                    }
            },
            "indefinidas": {},
        }


total_offenses = {
    "handwork": {
        "success": {
            "low": [],
            "mean": [],
            "high": []
        },
        "fails": {

            "low": [],
            "mean": [],
            "high": []
        }
    },
    "automatic": {
        "success": {
            "low": [],
            "mean": [],
            "high": []
        },
        "fails": {
            "low": [],
            "mean": [],
            "high": []
        }
    },
    "handwork_total": [],
    "handwork_success": [],
    "handwork_fails": [],
    "handwork_low": [],
    "handwork_mean": [],
    "handwork_high": [],
    "automatic_total": [],
    "automatic_success": [],
    "automatic_fails": [],
    "automatic_low": [],
    "automatic_mean": [],
    "automatic_high": [],
    "indefinidas": [],
    "total": [],
    "comprobacion": []
}

month = "01"
# Inicializar las variables np
variables = ["handwork_total",
    "handwork_success",
    "handwork_fails",
    "handwork_low",
    "handwork_mean",
    "handwork_high",
    "automatic_total",
    "automatic_success",
    "automatic_fails",
    "automatic_low",
    "automatic_mean",
    "automatic_high",
    "indefinidas",
    "total",
    "comprobacion"
]

for variable in variables:
    total_offenses[variable] = len(ticket_offenses_year[month])*[0]

for day in ticket_offenses_year[month]:
    total_offenses["handwork"]["success"]["low"].append(len(ticket_offenses_year[month][day]["handwork"]["success"]["low"]))
    total_offenses["handwork"]["success"]["mean"].append(len(ticket_offenses_year[month][day]["handwork"]["success"]["mean"]))
    total_offenses["handwork"]["success"]["high"].append(len(ticket_offenses_year[month][day]["handwork"]["success"]["high"]))
    total_offenses["handwork"]["fails"]["low"].append(len(ticket_offenses_year[month][day]["handwork"]["fails"]["low"]))
    total_offenses["handwork"]["fails"]["mean"].append(len(ticket_offenses_year[month][day]["handwork"]["fails"]["mean"]))
    total_offenses["handwork"]["fails"]["high"].append(len(ticket_offenses_year[month][day]["handwork"]["fails"]["high"]))
    total_offenses["automatic"]["success"]["low"].append(len(ticket_offenses_year[month][day]["automatic"]["success"]["low"]))
    total_offenses["automatic"]["success"]["mean"].append(len(ticket_offenses_year[month][day]["automatic"]["success"]["mean"]))
    total_offenses["automatic"]["success"]["high"].append(len(ticket_offenses_year[month][day]["automatic"]["success"]["high"]))
    total_offenses["automatic"]["fails"]["low"].append(len(ticket_offenses_year[month][day]["automatic"]["fails"]["low"]))
    total_offenses["automatic"]["fails"]["mean"].append(len(ticket_offenses_year[month][day]["automatic"]["fails"]["mean"]))
    total_offenses["automatic"]["fails"]["high"].append(len(ticket_offenses_year[month][day]["automatic"]["fails"]["high"]))
    total_offenses["indefinidas"].append(len(ticket_offenses_year[month][day]["indefinidas"]))
    total_offenses["handwork_total"] += (np.array(total_offenses["handwork"]["success"]["low"])
        + np.array(total_offenses["handwork"]["success"]["mean"])
        + np.array(total_offenses["handwork"]["success"]["high"])
        + np.array(total_offenses["handwork"]["fails"]["low"])
        + np.array(total_offenses["handwork"]["fails"]["mean"])
        + np.array(total_offenses["handwork"]["fails"]["high"])
    )
    total_offenses["handwork_success"] += (np.array(total_offenses["handwork"]["success"]["low"])
        + np.array(total_offenses["handwork"]["success"]["mean"])
        + np.array(total_offenses["handwork"]["success"]["high"])
    )
    total_offenses["handwork_fails"] += (np.array(total_offenses["handwork"]["fails"]["low"])
        + np.array(total_offenses["handwork"]["fails"]["mean"])
        + np.array(total_offenses["handwork"]["fails"]["high"])
    )
    total_offenses["handwork_low"] += (np.array(total_offenses["handwork"]["success"]["low"])
        + np.array(total_offenses["handwork"]["fails"]["low"])
    )
    total_offenses["handwork_mean"] += (np.array(total_offenses["handwork"]["success"]["mean"])
        + np.array(total_offenses["handwork"]["fails"]["mean"])
    )
    total_offenses["handwork_high"] += (np.array(total_offenses["handwork"]["success"]["high"])
        + np.array(total_offenses["handwork"]["fails"]["high"])
    )
    total_offenses["automatic_total"] += (np.array(total_offenses["automatic"]["success"]["low"])
        + np.array(total_offenses["automatic"]["success"]["mean"])
        + np.array(total_offenses["automatic"]["success"]["high"])
        + np.array(total_offenses["automatic"]["fails"]["low"])
        + np.array(total_offenses["automatic"]["fails"]["mean"])
        + np.array(total_offenses["automatic"]["fails"]["high"])
    )
    total_offenses["automatic_success"] += (np.array(total_offenses["automatic"]["success"]["low"])
        + np.array(total_offenses["automatic"]["success"]["mean"])
        + np.array(total_offenses["automatic"]["success"]["high"])
    )
    total_offenses["automatic_fails"] += (np.array(total_offenses["automatic"]["fails"]["low"])
        + np.array(total_offenses["automatic"]["fails"]["mean"])
        + np.array(total_offenses["automatic"]["fails"]["high"])
    )
    total_offenses["automatic_low"] += (np.array(total_offenses["automatic"]["success"]["low"])
        + np.array(total_offenses["automatic"]["fails"]["low"])
    )
    total_offenses["automatic_mean"] += (np.array(total_offenses["automatic"]["success"]["mean"])
        + np.array(total_offenses["automatic"]["fails"]["mean"])
    )
    total_offenses["automatic_high"] += (np.array(total_offenses["automatic"]["success"]["high"])
        + np.array(total_offenses["automatic"]["fails"]["high"])
    )
    total_offenses["total"] += (np.array(total_offenses["handwork"]["success"]["low"])
        + np.array(total_offenses["handwork"]["success"]["mean"])
        + np.array(total_offenses["handwork"]["success"]["high"])
        + np.array(total_offenses["handwork"]["fails"]["low"])
        + np.array(total_offenses["handwork"]["fails"]["mean"])
        + np.array(total_offenses["handwork"]["fails"]["high"])
        + np.array(total_offenses["automatic"]["success"]["low"])
        + np.array(total_offenses["automatic"]["success"]["mean"])
        + np.array(total_offenses["automatic"]["success"]["high"])
        + np.array(total_offenses["automatic"]["fails"]["low"])
        + np.array(total_offenses["automatic"]["fails"]["mean"])
        + np.array(total_offenses["automatic"]["fails"]["high"])
        + np.array(total_offenses["indefinidas"])
    )
    total_offenses["comprobacion"] += (np.array(total_offenses["handwork_total"])
        + np.array(total_offenses["automatic_total"])
        + np.array(total_offenses["indefinidas"])
    )
    
print(total_offenses)

    
            
            
            # if types_offenses == "handwork":
            #     total_offenses["handwork_total"][types_offenses].append(len(ticket_offenses_year["01"][day][types_offenses]))
            #     if level_offenses == "low":
            #         total_offenses["handwork_low"].append(len(ticket_offenses_year["01"][day][types_offenses]))
            #     elif types_offenses == "mean":
            #         total_offenses["automatic_total"].append(len(ticket_offenses_year["01"][day][types_offenses]))
            #     elif types_offenses == "indefinidas":
            #         total_offenses["indefinidas"].append(len(ticket_offenses_year["01"][day][types_offenses]))
        
        # for success_offenses in ticket_offenses_year["01"][types_offenses]:
        #     if types_offenses == "handwork" and success_offenses == "success":
        #             handwork_success = 0
        #         for level_offenses in  ticket_offenses_year["01"][types_offenses][success_offenses]:
        #             handwork_low = 0
        #             handwork_mean": 1,
        # "handwork_high": 1,
                
        #             if len(ticket_offenses_year["01"][types_offenses][success_offenses])
                
        #         else:

print("----")          
pprint(total_offenses)
