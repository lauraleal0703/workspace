import os
import json
import tools_data
import numpy as np

from datetime import datetime


os.system('clear')
inicio = datetime.now()

    
years = [2022]
for year in years:
    inicio_year = datetime.now()
    print(f"Inicio del año {year} -- {inicio_year}")
    path_ticket_offenses_year = os.path.join("data_collected", f"ticket_offenses_year_{year}.json")
    ticket_offenses_year = open(path_ticket_offenses_year)
    ticket_offenses_year = json.load(ticket_offenses_year)
    total_offenses = {}
    for month in ticket_offenses_year:
        inicio_month = datetime.now()
        print(f"Inicio del año y mes {year}-{month} -- {inicio_month}")
        # Inicializar el diccionario del mes
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
        print(f"Fin {year}-{month}")
        print(f"Tiempo de ejecución {datetime.now()-inicio_year}")
        tools_data.save_data_json(f"total_offenses_{month}", total_offenses, "data_collected/", year)
    
    print(total_offenses)
    print(f"Fin {year}-{month}")
    print(f"Tiempo de ejecución {datetime.now()-inicio_year}")


print(f"Tiempo de ejecución {datetime.now()-inicio}")
print("---Fin---")