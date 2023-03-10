import os
import re
import db
import tools_data
import tools_qradar

from models import Ticket
from pprint import pprint
from datetime import datetime, timedelta


os.system('clear')
inicio = datetime.now()

"""
Por medio de este archivo se hace una recopilacion de información
entre los datos obtenidos en Qradar y el ticket generado en OTRS
"""

years = [2022, 2021, 2020, 2019, 2018]
years = [2023]
for year in years:
    print(f"------{year}--------")
    # Inicializar el diccionario del año
    ticket_offenses_year = {}

    # Definir el periodo que se quiere consultar
    list_date = tools_data.list_date(datetime(year,1,1), datetime(year,1,23))

    # Recorrer cada uno de los días 
    for date in list_date:
        inicio_date = datetime.now()
        print(f"Inicio {inicio_date} ---> {date}")
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
                    },
                    "undefined": {
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
                    },
                    "undefined": {
                        "low": {},
                        "mean": {},
                        "high": {}
                    }
                },
                "undefined": {}
            }
        
        # Obtenter la data de OTRS según date
        data_otrs = db.session.query(Ticket).filter(
                        Ticket.create_time>=f"{date} 00:00:00",
                        Ticket.create_time<f"{date} 23:00:00")

        # Recorrer cada ticket generado en OTRS para sacar su id 
        # Con ese id ingresar a QRadar y obtener la fecha de inicio
        # Con las fechas ya obtenidad hacer el calculo del SLA de respuesta
        for ticket in data_otrs:
            if len(re.findall(r"Ofensa", ticket.title)) > 0 and len(re.findall(r"\d{5,}", ticket.title)) > 0 and len(set(re.findall(r"\d{5,}|-|\d{5,}", ticket.title))) == 2:
                id_offense = re.findall(r"\d{5,}", ticket.title)
                data_qradar = tools_qradar.start_time_offenses(id_offense[0])
                create_time_otrs = ticket.create_time + timedelta(hours=1)
                start_time_qradar = "0"
                response_time = "0"
                print(f" id_offense: {id_offense[0]} --create_time_otrs:{create_time_otrs} --data_qradar:{data_qradar}")
                handwork = re.findall(r"Ofensa N°", ticket.title)
                if handwork:
                    if data_qradar:
                        start_time_qradar = datetime.fromtimestamp(data_qradar)
                        response_time = create_time_otrs - start_time_qradar
                        ideal_response_time = timedelta(minutes=15)
                        if response_time <= ideal_response_time:
                            if len(re.findall(r"Criticidad|Baja", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["success"]["low"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            elif len(re.findall(r"Criticidad|Media", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["success"]["mean"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            elif len(re.findall(r"Criticidad|Alta", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["success"]["high"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            else:
                                print(f"---Alert handwork success {ticket.tn} {ticket.title}")
                        else:
                            if len(re.findall(r"Criticidad|Baja", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["fails"]["low"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            elif len(re.findall(r"Criticidad|Media", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["fails"]["mean"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            elif len(re.findall(r"Criticidad|Alta", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["fails"]["high"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            else:
                                print(f"---Alert handwork fails {ticket.tn} {ticket.title}")
                    else:
                        if len(re.findall(r"Criticidad|Baja", ticket.title)) > 1:
                            ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["undefined"]["low"][ticket.tn] = {
                                "id_qradar": id_offense[0],
                                "id_otrs": ticket.id,
                                "title": ticket.title,
                                "start_time": str(start_time_qradar),
                                "create_time": str(create_time_otrs),
                                "response_time": str(response_time)
                            }
                        elif len(re.findall(r"Criticidad|Media", ticket.title)) > 1:
                            ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["undefined"]["mean"][ticket.tn] = {
                                "id_qradar": id_offense[0],
                                "id_otrs": ticket.id,
                                "title": ticket.title,
                                "start_time": str(start_time_qradar),
                                "create_time": str(create_time_otrs),
                                "response_time": str(response_time)
                            }
                        elif len(re.findall(r"Criticidad|Alta", ticket.title)) > 1:
                            ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["handwork"]["undefined"]["high"][ticket.tn] = {
                                "id_qradar": id_offense[0],
                                "id_otrs": ticket.id,
                                "title": ticket.title,
                                "start_time": str(start_time_qradar),
                                "create_time": str(create_time_otrs),
                                "response_time": str(response_time)
                            }
                else:
                    if data_qradar:
                        start_time_qradar = datetime.fromtimestamp(data_qradar)
                        response_time = create_time_otrs - start_time_qradar
                        ideal_response_time = timedelta(minutes=15)
                        if response_time <= ideal_response_time:
                            if len(re.findall(r"Criticidad|Baja", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["success"]["low"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            elif len(re.findall(r"Criticidad|Media", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["success"]["mean"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            elif len(re.findall(r"Criticidad|Alta", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["success"]["high"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            else:
                                print(f"---Alert automatic success {ticket.tn} {ticket.title}")
                        else:
                            if len(re.findall(r"Criticidad|Baja", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["fails"]["low"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            elif len(re.findall(r"Criticidad|Media", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["fails"]["mean"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            elif len(re.findall(r"Criticidad|Alta", ticket.title)) > 1:
                                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["fails"]["high"][ticket.tn] = {
                                    "id_qradar": id_offense[0],
                                    "id_otrs": ticket.id,
                                    "title": ticket.title,
                                    "start_time": str(start_time_qradar),
                                    "create_time": str(create_time_otrs),
                                    "response_time": str(response_time)
                                }
                            else:
                                print(f"---Alert automatic fails {ticket.tn} {ticket.title}")
                    else:
                        if len(re.findall(r"Criticidad|Baja", ticket.title)) > 1:
                            ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["undefined"]["low"][ticket.tn] = {
                                "id_qradar": id_offense[0],
                                "id_otrs": ticket.id,
                                "title": ticket.title,
                                "start_time": str(start_time_qradar),
                                "create_time": str(create_time_otrs),
                                "response_time": str(response_time)
                            }
                        elif len(re.findall(r"Criticidad|Media", ticket.title)) > 1:
                            ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["undefined"]["mean"][ticket.tn] = {
                                "id_qradar": id_offense[0],
                                "id_otrs": ticket.id,
                                "title": ticket.title,
                                "start_time": str(start_time_qradar),
                                "create_time": str(create_time_otrs),
                                "response_time": str(response_time)
                            }
                        elif len(re.findall(r"Criticidad|Alta", ticket.title)) > 1:
                            ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["automatic"]["undefined"]["high"][ticket.tn] = {
                                "id_qradar": id_offense[0],
                                "id_otrs": ticket.id,
                                "title": ticket.title,
                                "start_time": str(start_time_qradar),
                                "create_time": str(create_time_otrs),
                                "response_time": str(response_time)
                            }
            else:
                ticket_offenses_year[date.split("-")[1]][date.split("-")[2]]["undefined"][ticket.tn] = {
                    "id": ticket.id,
                    "title": ticket.title,
                    "star_time": str(ticket.create_time)
                }
                print(ticket.tn, ticket.id, ticket.title)
        
        fin_date = datetime.now()
        print(f"Fin {fin_date} ---> {date}")
        print(f"Tiempo de ejecución {fin_date-inicio_date}")
        print("\n")
    
    tools_data.save_data_json(f"ticket_offenses_year_{year}", ticket_offenses_year)

print(f"Tiempo de ejecución {datetime.now()-inicio}")
print("---Fin---")