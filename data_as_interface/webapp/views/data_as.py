from flask import Blueprint
from flask import render_template
from flask import request
from flask import current_app

import os
import re
import json
import statistics
import numpy  as np


data_as = Blueprint("data_as", __name__, url_prefix="/data_as")


@data_as.get("/")
def index():
    current_folder = os.path.join(current_app.root_path, "static", "data_storage", "data_as")
    if request.method == "GET":
        year = request.args.get("year")
        month = request.args.get("month")

        if year and not month:
            file_path = os.path.join(current_folder, year, f"ticket_offenses_{year}.json")
            data_year = open(file_path)
            data_year = json.load(data_year)

            x_month = data_year[year].keys()
            y_counts = len(x_date)*[0]
            for month in data_year:
                y_counts = y_counts + np.array(data_year[month])

            



            x_date = data_month["offenses_handwork_low_successes"]["dates"]
            y_counts = len(x_date)*[0]

            cases_statistics = ['Promedio', 'Máximo', 'Mínimo']

            ##################--KPI N° 1--####################
            ## Número total de incidentes de seguridad ##

            # Grafica con el total de tickets
            for type_case in data_month:
                y_counts = y_counts + np.array(data_month[type_case]["counts"])
            
            y_counts = list(y_counts)
            total=str(sum(y_counts))
            cases_statistics_total = [statistics.mean(y_counts), max(y_counts), (min(y_counts))]

            # Grafica con el total de tickets manuales
            y_counts_handwork = len(x_date)*[0]
            for type_case in data_month:
                if len(re.findall(r"handwork", type_case)) > 0:
                    y_counts_handwork = y_counts_handwork + np.array(data_month[type_case]["counts"])
            y_counts_handwork = list(y_counts_handwork)
            cases_statistics_manual = [statistics.mean(y_counts_handwork), max(y_counts_handwork), min(y_counts_handwork)]


            # Grafica con el total de tickets automaticas
            y_counts_automatic = len(x_date)*[0]
            for type_case in data_month:
                if len(re.findall(r"automatic", type_case)) > 0:
                    y_counts_automatic = y_counts_automatic + np.array(data_month[type_case]["counts"])
            y_counts_automatic = list(y_counts_automatic)
            cases_statistics_automatica = [statistics.mean(y_counts_automatic), max(y_counts_automatic), min(y_counts_automatic)]

            return render_template(
                "data_as/index.html",
                page={"title": "Data Adaptive Security"},
                total=total,
                y_counts=y_counts,
                y_counts_handwork=y_counts_handwork,
                y_counts_automatic=y_counts_automatic,
                cases_statistics=cases_statistics,
                cases_statistics_total=cases_statistics_total,
                cases_statistics_manual=cases_statistics_manual,
                cases_statistics_automatica=cases_statistics_automatica
            )

        return render_template(
            "data_as/index.html",
            page={"title": "Data Adaptive Security"}
        )