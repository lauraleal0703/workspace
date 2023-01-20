import os
import re
import json
import numpy as np
import statistics

from datetime import datetime
import matplotlib.pyplot as plt

##Crear la carpeta de "graphs" donde se guardaran los graficos
os.system('clear')
inicio = datetime.now()
print(f"Inicio {inicio}")

year = "2022"
month = "12"
path_data_json = f"data_leaked/{year}/data_month_{month}.json"
data_month = open(path_data_json)
data_month = json.load(data_month)

x_date = data_month["offenses_handwork_low_successes"]["dates"]
y_counts = len(x_date)*[0]

##################--KPI N° 1--####################
## Número total de incidentes de seguridad ##

# Grafica con el total de tickets
for type_case in data_month:
    y_counts = y_counts + np.array(data_month[type_case]["counts"])

# Grafica con el total de tickets manuales
y_counts_handwork = len(x_date)*[0]
for type_case in data_month:
    if len(re.findall(r"handwork", type_case)) > 0:
        y_counts_handwork = y_counts_handwork + np.array(data_month[type_case]["counts"])

# Grafica con el total de tickets automaticas
y_counts_automatic = len(x_date)*[0]
for type_case in data_month:
    if len(re.findall(r"automatic", type_case)) > 0:
        y_counts_automatic = y_counts_automatic + np.array(data_month[type_case]["counts"])

plt.plot(x_date, y_counts, label=f"Total --> Promedio={statistics.mean(y_counts)} Máx={max(y_counts)} Mín={min(y_counts)}")
plt.plot(x_date, y_counts_handwork, label=f"Manuales --> Promedio={statistics.mean(y_counts_handwork)} Máx={max(y_counts_handwork)} Mín={min(y_counts_handwork)}")
plt.plot(x_date, y_counts_automatic, label=f"Automáticas --> Promedio={statistics.mean(y_counts_automatic)} Máx={max(y_counts_automatic)} Mín={min(y_counts_automatic)}")
plt.xticks(x_date, x_date, rotation=90, fontsize=8)
plt.yticks(fontsize=8)
plt.legend(loc="upper center", fontsize=8)
plt.grid()
plt.tick_params(axis="both", which="both", labelsize=8)
plt.title(f"Número total de incidentes de seguridad {sum(y_counts)}", fontsize=8)
plt.savefig(f"graphs/kpi_1_total_incidents_month_{month}.png", dpi=300, bbox_inches='tight')


print(f"Tiempo de ejecución {datetime.now()-inicio}")
print("---Fin---")