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

customers = ["AAN",
    "Adaptive Security",
    "BDO",
    "CAS",
    "EMSA",
    "EVERTEC",
    "Evertec",
    "SBPay",
    "SBPAY",
    "SURA",
    "UDLA",
    "AS",
    "CMPC",
    "CCA",
    "CYT",
    "UDP",
    "UAI",
    "SINACOFI",
    "Fwd",
    "Re:",
    "RE:",
    "RV:",
    "Undefined"
]

admin = ['Solange Aravena H.',
    'Miguel González M.',
    'Francisco Sepulveda',
    'Miguel Almendra V.',
    'Andrés Rojas',
    'Diego Orellana V.',
    'Jose Nicolas',
    'Nicolas Garrido',
    'Dorian Malfert M.',
    'Admin OTRS',
    'Cristopher Ulloa',
    'Sugy Nam',
    'Mauricio Retamales',
    'Jonathan Finschi'
]

years = [2022, 2021, 2020, 2019, 2018]
years = [2023]
for year in years:
    print(f"------{year}--------")
    # Inicializar el diccionario del año
    ticket_customer_year = {}
    ticket_admin_year = {}

    for customer in customers:
        ticket_customer_year[customer] = {}

    # Definir el periodo que se quiere consultar
    list_date = tools_data.list_date(datetime(year,1,1), datetime(year,1,10))

    # Recorrer cada uno de los días 
    for date in list_date:
        inicio_date = datetime.now()
        print(f"Inicio {inicio_date} ---> {date}")

        # Obtenter la data de OTRS según date
        # data_otrs = db.session.query(Ticket).filter(
        #                 Ticket.queue_id == 6,
        #                 Ticket.create_time>=f"{date} 00:00:00",
        #                 Ticket.create_time<f"{date} 23:00:00").all()
        data_otrs = Ticket.tickets_by_date(6, date)
       
        # Recorrer cada ticket generado en OTRS para sacar su id 
        # Con ese id ingresar a QRadar y obtener la fecha de inicio
        # Con las fechas ya obtenidad hacer el calculo del SLA de respuesta
        for ticket in data_otrs:
            name_admin = ticket.user.full_name
            if name_admin not in ticket_admin_year:
                ticket_admin_year[name_admin] = {}
            if int(date.split("-")[1]) not in ticket_admin_year[name_admin]:
                ticket_admin_year[name_admin][int(date.split("-")[1])] = {}

            for customer in customers:
                value = 0
                if len(re.findall(customer, ticket.title)) > 0:
                    value = 1
                    break
            if value == 0:
                customer = "Undefined"
            
            if int(date.split("-")[1]) not in ticket_customer_year[customer]:
                ticket_customer_year[customer][int(date.split("-")[1])]  = {}
            
            print(name_admin, customer)

            create_time_otrs = ticket.create_time + timedelta(hours=1)
            change_time = ticket.change_time + timedelta(hours=1)
            response_time = "0"
            print(f"tiempo se solucion {change_time-create_time_otrs}\n")

''''
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
'''
print(f"Tiempo de ejecución {datetime.now()-inicio}")
print("---Fin---")