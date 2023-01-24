import os
import json
import tools_data
import numpy as np

from datetime import datetime
from pprint import pprint


os.system('clear')
inicio = datetime.now()

    
years = [2023, 2022, 2021, 2020, 2019, 2018]
for year in years:
    total_offenses_year = {}
    inicio_year = datetime.now()
    print(f"Inicio del año {year} -- {inicio_year}")
    total_offenses_year = {
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
            },
            "undefined": {
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
            },
            "undefined": {
                "low": [],
                "mean": [],
                "high": []
            }
        },
        "handwork_total": [],
        "handwork_success": [],
        "handwork_fails": [],
        "handwork_undefined": [],
        "handwork_low": [],
        "handwork_mean": [],
        "handwork_high": [],
        "automatic_total": [],
        "automatic_success": [],
        "automatic_fails": [],
        "automatic_undefined": [],
        "automatic_low": [],
        "automatic_mean": [],
        "automatic_high": [],
        "undefined": [],
        "total": [],
        "handwork_total_sum": 0,
        "handwork_success_sum": 0,
        "handwork_fails_sum": 0,
        "handwork_undefined_sum": 0,
        "handwork_low_sum": 0,
        "handwork_mean_sum": 0,
        "handwork_high_sum": 0,
        "automatic_total_sum": 0,
        "automatic_success_sum": 0,
        "automatic_fails_sum": 0,
        "automatic_undefined_sum": 0,
        "automatic_low_sum": 0,
        "automatic_mean_sum": 0,
        "automatic_high_sum": 0,
        "undefined_sum": 0,
        "total_sum": 0
    }

    variables = ["handwork_total",
        "handwork_success",
        "handwork_fails",
        "handwork_undefined",
        "handwork_low",
        "handwork_mean",
        "handwork_high",
        "automatic_total",
        "automatic_success",
        "automatic_fails",
        "automatic_undefined",
        "automatic_low",
        "automatic_mean",
        "automatic_high",
        "total"
    ]

    path_ticket_offenses_year = os.path.join("data_collected", f"ticket_offenses_year_{year}.json")
    ticket_offenses_year = open(path_ticket_offenses_year)
    ticket_offenses_year = json.load(ticket_offenses_year)

    total_offenses = {}
    for month in ticket_offenses_year:
        print(f"-------> {month}")
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
                },
                "undefined": {
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
                },
                "undefined": {
                    "low": [],
                    "mean": [],
                    "high": []
                }
            },
            "handwork_total": [],
            "handwork_success": [],
            "handwork_fails": [],
            "handwork_undefined": [],
            "handwork_low": [],
            "handwork_mean": [],
            "handwork_high": [],
            "automatic_total": [],
            "automatic_success": [],
            "automatic_fails": [],
            "automatic_undefined": [],
            "automatic_low": [],
            "automatic_mean": [],
            "automatic_high": [],
            "undefined": [],
            "total": [],
            "handwork_total_sum": 0,
            "handwork_success_sum": 0,
            "handwork_fails_sum": 0,
            "handwork_undefined_sum": 0,
            "handwork_low_sum": 0,
            "handwork_mean_sum": 0,
            "handwork_high_sum": 0,
            "automatic_total_sum": 0,
            "automatic_success_sum": 0,
            "automatic_fails_sum": 0,
            "automatic_undefined_sum": 0,
            "automatic_low_sum": 0,
            "automatic_mean_sum": 0,
            "automatic_high_sum": 0,
            "undefined_sum": 0,
            "total_sum": 0
        }

        for day in ticket_offenses_year[month]:
            total_offenses["handwork"]["success"]["low"].append(len(ticket_offenses_year[month][day]["handwork"]["success"]["low"]))
            total_offenses["handwork"]["success"]["mean"].append(len(ticket_offenses_year[month][day]["handwork"]["success"]["mean"]))
            total_offenses["handwork"]["success"]["high"].append(len(ticket_offenses_year[month][day]["handwork"]["success"]["high"]))
            total_offenses["handwork"]["fails"]["low"].append(len(ticket_offenses_year[month][day]["handwork"]["fails"]["low"]))
            total_offenses["handwork"]["fails"]["mean"].append(len(ticket_offenses_year[month][day]["handwork"]["fails"]["mean"]))
            total_offenses["handwork"]["fails"]["high"].append(len(ticket_offenses_year[month][day]["handwork"]["fails"]["high"]))
            total_offenses["handwork"]["undefined"]["low"].append(len(ticket_offenses_year[month][day]["handwork"]["undefined"]["low"]))
            total_offenses["handwork"]["undefined"]["mean"].append(len(ticket_offenses_year[month][day]["handwork"]["undefined"]["mean"]))
            total_offenses["handwork"]["undefined"]["high"].append(len(ticket_offenses_year[month][day]["handwork"]["undefined"]["high"]))
            total_offenses["automatic"]["success"]["low"].append(len(ticket_offenses_year[month][day]["automatic"]["success"]["low"]))
            total_offenses["automatic"]["success"]["mean"].append(len(ticket_offenses_year[month][day]["automatic"]["success"]["mean"]))
            total_offenses["automatic"]["success"]["high"].append(len(ticket_offenses_year[month][day]["automatic"]["success"]["high"]))
            total_offenses["automatic"]["fails"]["low"].append(len(ticket_offenses_year[month][day]["automatic"]["fails"]["low"]))
            total_offenses["automatic"]["fails"]["mean"].append(len(ticket_offenses_year[month][day]["automatic"]["fails"]["mean"]))
            total_offenses["automatic"]["fails"]["high"].append(len(ticket_offenses_year[month][day]["automatic"]["fails"]["high"]))
            total_offenses["automatic"]["undefined"]["low"].append(len(ticket_offenses_year[month][day]["automatic"]["undefined"]["low"]))
            total_offenses["automatic"]["undefined"]["mean"].append(len(ticket_offenses_year[month][day]["automatic"]["undefined"]["mean"]))
            total_offenses["automatic"]["undefined"]["high"].append(len(ticket_offenses_year[month][day]["automatic"]["undefined"]["high"]))
            total_offenses["undefined"].append(len(ticket_offenses_year[month][day]["undefined"]))

        total_offenses_year["handwork"]["success"]["low"].append(sum(total_offenses["handwork"]["success"]["low"]))
        total_offenses_year["handwork"]["success"]["mean"].append(sum(total_offenses["handwork"]["success"]["mean"]))
        total_offenses_year["handwork"]["success"]["high"].append(sum(total_offenses["handwork"]["success"]["high"]))
        total_offenses_year["handwork"]["fails"]["low"].append(sum(total_offenses["handwork"]["fails"]["low"]))
        total_offenses_year["handwork"]["fails"]["mean"].append(sum(total_offenses["handwork"]["fails"]["mean"]))
        total_offenses_year["handwork"]["fails"]["high"].append(sum(total_offenses["handwork"]["fails"]["high"]))
        total_offenses_year["handwork"]["undefined"]["low"].append(sum(total_offenses["handwork"]["undefined"]["low"]))
        total_offenses_year["handwork"]["undefined"]["mean"].append(sum(total_offenses["handwork"]["undefined"]["mean"]))
        total_offenses_year["handwork"]["undefined"]["high"].append(sum(total_offenses["handwork"]["undefined"]["high"]))
        total_offenses_year["automatic"]["success"]["low"].append(sum(total_offenses["automatic"]["success"]["low"]))
        total_offenses_year["automatic"]["success"]["mean"].append(sum(total_offenses["automatic"]["success"]["mean"]))
        total_offenses_year["automatic"]["success"]["high"].append(sum(total_offenses["automatic"]["success"]["high"]))
        total_offenses_year["automatic"]["fails"]["low"].append(sum(total_offenses["automatic"]["fails"]["low"]))
        total_offenses_year["automatic"]["fails"]["mean"].append(sum(total_offenses["automatic"]["fails"]["mean"]))
        total_offenses_year["automatic"]["fails"]["high"].append(sum(total_offenses["automatic"]["fails"]["high"]))
        total_offenses_year["automatic"]["undefined"]["low"].append(sum(total_offenses["automatic"]["undefined"]["low"]))
        total_offenses_year["automatic"]["undefined"]["mean"].append(sum(total_offenses["automatic"]["undefined"]["mean"]))
        total_offenses_year["automatic"]["undefined"]["high"].append(sum(total_offenses["automatic"]["undefined"]["high"]))
        total_offenses_year["undefined"].append(sum(total_offenses["undefined"]))
        
        total_offenses["undefined_sum"] = sum(total_offenses["undefined"])
        
        for variable in variables:
            total_offenses[variable] = len(ticket_offenses_year[month])*[0]

        total_offenses["handwork_total"] += (np.array(total_offenses["handwork"]["success"]["low"])
            + np.array(total_offenses["handwork"]["success"]["mean"])
            + np.array(total_offenses["handwork"]["success"]["high"])
            + np.array(total_offenses["handwork"]["fails"]["low"])
            + np.array(total_offenses["handwork"]["fails"]["mean"])
            + np.array(total_offenses["handwork"]["fails"]["high"])
            + np.array(total_offenses["handwork"]["undefined"]["low"])
            + np.array(total_offenses["handwork"]["undefined"]["mean"])
            + np.array(total_offenses["handwork"]["undefined"]["high"])
        )
        total_offenses["handwork_total"] = total_offenses["handwork_total"].tolist()
        total_offenses["handwork_total_sum"] = sum(total_offenses["handwork_total"])

        total_offenses["handwork_success"] += (np.array(total_offenses["handwork"]["success"]["low"])
            + np.array(total_offenses["handwork"]["success"]["mean"])
            + np.array(total_offenses["handwork"]["success"]["high"])
        )
        total_offenses["handwork_success"] = total_offenses["handwork_success"].tolist()
        total_offenses["handwork_success_sum"] = sum(total_offenses["handwork_success"])
        
        total_offenses["handwork_fails"] += (np.array(total_offenses["handwork"]["fails"]["low"])
            + np.array(total_offenses["handwork"]["fails"]["mean"])
            + np.array(total_offenses["handwork"]["fails"]["high"])
        )
        total_offenses["handwork_fails"] = total_offenses["handwork_fails"].tolist()
        total_offenses["handwork_fails_sum"] = sum(total_offenses["handwork_fails"])
        
        total_offenses["handwork_undefined"] += (np.array(total_offenses["handwork"]["undefined"]["low"])
            + np.array(total_offenses["handwork"]["undefined"]["mean"])
            + np.array(total_offenses["handwork"]["undefined"]["high"])
        )
        total_offenses["handwork_undefined"] = total_offenses["handwork_undefined"].tolist()
        total_offenses["handwork_undefined_sum"] = sum(total_offenses["handwork_undefined"])
        
        total_offenses["handwork_low"] += (np.array(total_offenses["handwork"]["success"]["low"])
            + np.array(total_offenses["handwork"]["fails"]["low"])
            + np.array(total_offenses["handwork"]["undefined"]["low"])
        )
        total_offenses["handwork_low"] = total_offenses["handwork_low"].tolist()
        total_offenses["handwork_low_sum"] = sum(total_offenses["handwork_low"])

        total_offenses["handwork_mean"] += (np.array(total_offenses["handwork"]["success"]["mean"])
            + np.array(total_offenses["handwork"]["fails"]["mean"])
            + np.array(total_offenses["handwork"]["undefined"]["mean"])
        )
        total_offenses["handwork_mean"] = total_offenses["handwork_mean"].tolist()
        total_offenses["handwork_mean_sum"] = sum(total_offenses["handwork_mean"])

        total_offenses["handwork_high"] += (np.array(total_offenses["handwork"]["success"]["high"])
            + np.array(total_offenses["handwork"]["fails"]["high"])
            + np.array(total_offenses["handwork"]["undefined"]["high"])
        )
        total_offenses["handwork_high"] = total_offenses["handwork_high"].tolist()
        total_offenses["handwork_high_sum"] = sum(total_offenses["handwork_high"])
        
        total_offenses["automatic_total"] += (np.array(total_offenses["automatic"]["success"]["low"])
            + np.array(total_offenses["automatic"]["success"]["mean"])
            + np.array(total_offenses["automatic"]["success"]["high"])
            + np.array(total_offenses["automatic"]["fails"]["low"])
            + np.array(total_offenses["automatic"]["fails"]["mean"])
            + np.array(total_offenses["automatic"]["fails"]["high"])
            + np.array(total_offenses["automatic"]["undefined"]["low"])
            + np.array(total_offenses["automatic"]["undefined"]["mean"])
            + np.array(total_offenses["automatic"]["undefined"]["high"])
        )
        total_offenses["automatic_total"] = total_offenses["automatic_total"].tolist()
        total_offenses["automatic_total_sum"] = sum(total_offenses["automatic_total"])

        total_offenses["automatic_success"] += (np.array(total_offenses["automatic"]["success"]["low"])
            + np.array(total_offenses["automatic"]["success"]["mean"])
            + np.array(total_offenses["automatic"]["success"]["high"])
        )
        total_offenses["automatic_success"] = total_offenses["automatic_success"].tolist()
        total_offenses["automatic_success_sum"] = sum(total_offenses["automatic_success"])

        total_offenses["automatic_fails"] += (np.array(total_offenses["automatic"]["fails"]["low"])
            + np.array(total_offenses["automatic"]["fails"]["mean"])
            + np.array(total_offenses["automatic"]["fails"]["high"])
        )
        total_offenses["automatic_fails"] = total_offenses["automatic_fails"].tolist()
        total_offenses["automatic_fails_sum"] = sum(total_offenses["automatic_fails"])

        total_offenses["automatic_undefined"] += (np.array(total_offenses["automatic"]["undefined"]["low"])
            + np.array(total_offenses["automatic"]["undefined"]["mean"])
            + np.array(total_offenses["automatic"]["undefined"]["high"])
        )
        total_offenses["automatic_undefined"] = total_offenses["automatic_undefined"].tolist()
        total_offenses["automatic_undefined_sum"] = sum(total_offenses["automatic_undefined"])

        total_offenses["automatic_low"] += (np.array(total_offenses["automatic"]["success"]["low"])
            + np.array(total_offenses["automatic"]["fails"]["low"])
            + np.array(total_offenses["automatic"]["undefined"]["low"])
        )
        total_offenses["automatic_low"] = total_offenses["automatic_low"].tolist()
        total_offenses["automatic_low_sum"] = sum(total_offenses["automatic_low"])

        total_offenses["automatic_mean"] += (np.array(total_offenses["automatic"]["success"]["mean"])
            + np.array(total_offenses["automatic"]["fails"]["mean"])
            + np.array(total_offenses["automatic"]["undefined"]["mean"])
        )
        total_offenses["automatic_mean"] = total_offenses["automatic_mean"].tolist()
        total_offenses["automatic_mean_sum"] = sum(total_offenses["automatic_mean"])
        
        total_offenses["automatic_high"] += (np.array(total_offenses["automatic"]["success"]["high"])
            + np.array(total_offenses["automatic"]["fails"]["high"])
            + np.array(total_offenses["automatic"]["undefined"]["high"])
        )
        total_offenses["automatic_high"] = total_offenses["automatic_high"].tolist()
        total_offenses["automatic_high_sum"] = sum(total_offenses["automatic_high"])

        total_offenses["total"] += (np.array(total_offenses["handwork"]["success"]["low"])
            + np.array(total_offenses["handwork"]["success"]["mean"])
            + np.array(total_offenses["handwork"]["success"]["high"])
            + np.array(total_offenses["handwork"]["fails"]["low"])
            + np.array(total_offenses["handwork"]["fails"]["mean"])
            + np.array(total_offenses["handwork"]["fails"]["high"])
            + np.array(total_offenses["handwork"]["undefined"]["low"])
            + np.array(total_offenses["handwork"]["undefined"]["mean"])
            + np.array(total_offenses["handwork"]["undefined"]["high"])
            + np.array(total_offenses["automatic"]["success"]["low"])
            + np.array(total_offenses["automatic"]["success"]["mean"])
            + np.array(total_offenses["automatic"]["success"]["high"])
            + np.array(total_offenses["automatic"]["fails"]["low"])
            + np.array(total_offenses["automatic"]["fails"]["mean"])
            + np.array(total_offenses["automatic"]["fails"]["high"])
            + np.array(total_offenses["automatic"]["undefined"]["low"])
            + np.array(total_offenses["automatic"]["undefined"]["mean"])
            + np.array(total_offenses["automatic"]["undefined"]["high"])
            + np.array(total_offenses["undefined"])
        )
        total_offenses["total"] = total_offenses["total"].tolist()
        total_offenses["total_sum"] = sum(total_offenses["total"])

        print(total_offenses)
        print(f"Fin {year}-{month}")
        print(f"Tiempo de ejecución {datetime.now()-inicio_month}")
        tools_data.save_data_json(f"total_offenses_month_{int(month)}", total_offenses, year)

    total_offenses_year["undefined_sum"]= sum(total_offenses_year["undefined"])

    for variable in variables:
        total_offenses_year[variable] = len(ticket_offenses_year)*[0]

    print(f'total_offenses_year["handwork_total"] {total_offenses_year["handwork_total"]} {len(total_offenses_year["handwork_total"])}')
    print(f'total_offenses_year["handwork"]["success"]["low"] {total_offenses_year["handwork"]["success"]["low"]}')
    total_offenses_year["handwork_total"] += (np.array(total_offenses_year["handwork"]["success"]["low"])
        + np.array(total_offenses_year["handwork"]["success"]["mean"])
        + np.array(total_offenses_year["handwork"]["success"]["high"])
        + np.array(total_offenses_year["handwork"]["fails"]["low"])
        + np.array(total_offenses_year["handwork"]["fails"]["mean"])
        + np.array(total_offenses_year["handwork"]["fails"]["high"])
        + np.array(total_offenses_year["handwork"]["undefined"]["low"])
        + np.array(total_offenses_year["handwork"]["undefined"]["mean"])
        + np.array(total_offenses_year["handwork"]["undefined"]["high"])
    )
    total_offenses_year["handwork_total"] = total_offenses_year["handwork_total"].tolist()
    total_offenses_year["handwork_total_sum"] = sum(total_offenses_year["handwork_total"])

    total_offenses_year["handwork_success"] += (np.array(total_offenses_year["handwork"]["success"]["low"])
        + np.array(total_offenses_year["handwork"]["success"]["mean"])
        + np.array(total_offenses_year["handwork"]["success"]["high"])
    )
    total_offenses_year["handwork_success"] = total_offenses_year["handwork_success"].tolist()
    total_offenses_year["handwork_success_sum"] = sum(total_offenses_year["handwork_success"])
    
    total_offenses_year["handwork_fails"] += (np.array(total_offenses_year["handwork"]["fails"]["low"])
        + np.array(total_offenses_year["handwork"]["fails"]["mean"])
        + np.array(total_offenses_year["handwork"]["fails"]["high"])
    )
    total_offenses_year["handwork_fails"] = total_offenses_year["handwork_fails"].tolist()
    total_offenses_year["handwork_fails_sum"] = sum(total_offenses_year["handwork_fails"])
    
    total_offenses_year["handwork_undefined"] += (np.array(total_offenses_year["handwork"]["undefined"]["low"])
        + np.array(total_offenses_year["handwork"]["undefined"]["mean"])
        + np.array(total_offenses_year["handwork"]["undefined"]["high"])
    )
    total_offenses_year["handwork_undefined"] = total_offenses_year["handwork_undefined"].tolist()
    total_offenses_year["handwork_undefined_sum"] = sum(total_offenses_year["handwork_undefined"])
    
    total_offenses_year["handwork_low"] += (np.array(total_offenses_year["handwork"]["success"]["low"])
        + np.array(total_offenses_year["handwork"]["fails"]["low"])
        + np.array(total_offenses_year["handwork"]["undefined"]["low"])
    )
    total_offenses_year["handwork_low"] = total_offenses_year["handwork_low"].tolist()
    total_offenses_year["handwork_low_sum"] = sum(total_offenses_year["handwork_low"])

    total_offenses_year["handwork_mean"] += (np.array(total_offenses_year["handwork"]["success"]["mean"])
        + np.array(total_offenses_year["handwork"]["fails"]["mean"])
        + np.array(total_offenses_year["handwork"]["undefined"]["mean"])
    )
    total_offenses_year["handwork_mean"] = total_offenses_year["handwork_mean"].tolist()
    total_offenses_year["handwork_mean_sum"] = sum(total_offenses_year["handwork_mean"])

    total_offenses_year["handwork_high"] += (np.array(total_offenses_year["handwork"]["success"]["high"])
        + np.array(total_offenses_year["handwork"]["fails"]["high"])
        + np.array(total_offenses_year["handwork"]["undefined"]["high"])
    )
    total_offenses_year["handwork_high"] = total_offenses_year["handwork_high"].tolist()
    total_offenses_year["handwork_high_sum"] = sum(total_offenses_year["handwork_high"])
    
    total_offenses_year["automatic_total"] += (np.array(total_offenses_year["automatic"]["success"]["low"])
        + np.array(total_offenses_year["automatic"]["success"]["mean"])
        + np.array(total_offenses_year["automatic"]["success"]["high"])
        + np.array(total_offenses_year["automatic"]["fails"]["low"])
        + np.array(total_offenses_year["automatic"]["fails"]["mean"])
        + np.array(total_offenses_year["automatic"]["fails"]["high"])
        + np.array(total_offenses_year["automatic"]["undefined"]["low"])
        + np.array(total_offenses_year["automatic"]["undefined"]["mean"])
        + np.array(total_offenses_year["automatic"]["undefined"]["high"])
    )
    total_offenses_year["automatic_total"] = total_offenses_year["automatic_total"].tolist()
    total_offenses_year["automatic_total_sum"] = sum(total_offenses_year["automatic_total"])

    total_offenses_year["automatic_success"] += (np.array(total_offenses_year["automatic"]["success"]["low"])
        + np.array(total_offenses_year["automatic"]["success"]["mean"])
        + np.array(total_offenses_year["automatic"]["success"]["high"])
    )
    total_offenses_year["automatic_success"] = total_offenses_year["automatic_success"].tolist()
    total_offenses_year["automatic_success_sum"] = sum(total_offenses_year["automatic_success"])

    total_offenses_year["automatic_fails"] += (np.array(total_offenses_year["automatic"]["fails"]["low"])
        + np.array(total_offenses_year["automatic"]["fails"]["mean"])
        + np.array(total_offenses_year["automatic"]["fails"]["high"])
    )
    total_offenses_year["automatic_fails"] = total_offenses_year["automatic_fails"].tolist()
    total_offenses_year["automatic_fails_sum"] = sum(total_offenses_year["automatic_fails"])

    total_offenses_year["automatic_undefined"] += (np.array(total_offenses_year["automatic"]["undefined"]["low"])
        + np.array(total_offenses_year["automatic"]["undefined"]["mean"])
        + np.array(total_offenses_year["automatic"]["undefined"]["high"])
    )
    total_offenses_year["automatic_undefined"] = total_offenses_year["automatic_undefined"].tolist()
    total_offenses_year["automatic_undefined_sum"] = sum(total_offenses_year["automatic_undefined"])

    total_offenses_year["automatic_low"] += (np.array(total_offenses_year["automatic"]["success"]["low"])
        + np.array(total_offenses_year["automatic"]["fails"]["low"])
        + np.array(total_offenses_year["automatic"]["undefined"]["low"])
    )
    total_offenses_year["automatic_low"] = total_offenses_year["automatic_low"].tolist()
    total_offenses_year["automatic_low_sum"] = sum(total_offenses_year["automatic_low"])

    total_offenses_year["automatic_mean"] += (np.array(total_offenses_year["automatic"]["success"]["mean"])
        + np.array(total_offenses_year["automatic"]["fails"]["mean"])
        + np.array(total_offenses_year["automatic"]["undefined"]["mean"])
    )
    total_offenses_year["automatic_mean"] = total_offenses_year["automatic_mean"].tolist()
    total_offenses_year["automatic_mean_sum"] = sum(total_offenses_year["automatic_mean"])
    
    total_offenses_year["automatic_high"] += (np.array(total_offenses_year["automatic"]["success"]["high"])
        + np.array(total_offenses_year["automatic"]["fails"]["high"])
        + np.array(total_offenses_year["automatic"]["undefined"]["high"])
    )
    total_offenses_year["automatic_high"] = total_offenses_year["automatic_high"].tolist()
    total_offenses_year["automatic_high_sum"] = sum(total_offenses_year["automatic_high"])

    total_offenses_year["total"] += (np.array(total_offenses_year["handwork"]["success"]["low"])
        + np.array(total_offenses_year["handwork"]["success"]["mean"])
        + np.array(total_offenses_year["handwork"]["success"]["high"])
        + np.array(total_offenses_year["handwork"]["fails"]["low"])
        + np.array(total_offenses_year["handwork"]["fails"]["mean"])
        + np.array(total_offenses_year["handwork"]["fails"]["high"])
        + np.array(total_offenses_year["handwork"]["undefined"]["low"])
        + np.array(total_offenses_year["handwork"]["undefined"]["mean"])
        + np.array(total_offenses_year["handwork"]["undefined"]["high"])
        + np.array(total_offenses_year["automatic"]["success"]["low"])
        + np.array(total_offenses_year["automatic"]["success"]["mean"])
        + np.array(total_offenses_year["automatic"]["success"]["high"])
        + np.array(total_offenses_year["automatic"]["fails"]["low"])
        + np.array(total_offenses_year["automatic"]["fails"]["mean"])
        + np.array(total_offenses_year["automatic"]["fails"]["high"])
        + np.array(total_offenses_year["automatic"]["undefined"]["low"])
        + np.array(total_offenses_year["automatic"]["undefined"]["mean"])
        + np.array(total_offenses_year["automatic"]["undefined"]["high"])
        + np.array(total_offenses_year["undefined"])
    )
    total_offenses_year["total"] = total_offenses_year["total"].tolist()
    total_offenses_year["total_sum"] = sum(total_offenses_year["total"])
    
    print(total_offenses_year)
    print(f"Fin {year}")
    print(f"Tiempo de ejecución {datetime.now()-inicio_year}")
    tools_data.save_data_json(f"total_offenses_year_{year}", total_offenses_year, year)

print(f"Tiempo de ejecución {datetime.now()-inicio}")
print("---Fin---")