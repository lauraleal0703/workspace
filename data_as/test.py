import db
import tools_qradar

from models import Ticket
from pprint import pprint
from datetime import datetime

import os
import re

os.system('clear')


# print(">>---------Prueba personalizada---------------")

# data_otrs = db.session.query(Ticket).filter(Ticket.tn == 2023010254001055).first()
# print(data_otrs.title)
# print(data_otrs.create_time)

# data_qradar = tools_qradar.offenses(
#                 params={
#                     "fields": "start_time",
#                     "filter": f"id=64905"
#                     }
#                 )
# epoch = data_qradar[0]["start_time"]
# fecha_chl = tools_qradar.epoch2date_mili(epoch)
# print(fecha_chl)


print(">>---------OTRS-->-----QRadar---------")

data_otrs = db.session.query(Ticket).filter(
                Ticket.create_time < "2023-01-01", Ticket.create_time > "2022-12-30").all()

dict_id_ofensas = {}
for ticket in data_otrs:
    manual = re.findall(r"°", ticket.title)
    
    if manual:
        id_ofensa = re.findall(r"(\d{5,})]", ticket.title)
        criticidad = re.findall(r"Criticidad:", ticket.title)
        
        if id_ofensa and criticidad:
            tipo_criticidad = re.findall(r":\w+", ticket.title)

            print(type(id_ofensa), id_ofensa)

            exit()
            
            if not tipo_criticidad:
                tipo_criticidad = re.findall(r": \w+", ticket.title)
            
            data_qradar = tools_qradar.offenses(
                    params={
                        "fields": "start_time",
                        "filter": f"id={int(id_ofensa)}"
                        }
                    )
            
            start_time_qradar = datetime.fromtimestamp(int(data_qradar[0]["start_time"])/1000)
            
            print(type(start_time_qradar), start_time_qradar)
            print(type(ticket.create_time), ticket.create_time)

            dict_id_ofensas[id_ofensa[0]] = [
                ticket.id, 
                list(tipo_criticidad[0].split(":"))[1], 
                ticket.tn, 
                ticket.create_time]

pprint(dict_id_ofensas)

# for ticket in dict_id_ofensa.keys():
#     print(ticket)
#     pprint(dict_id_ofensa[ticket])
#     tiempo_respuesta = dict_id_ofensa[ticket][-2] - dict_id_ofensa[ticket][-1]
#     print(tiempo_respuesta, type(tiempo_respuesta))
#     print("-------------")

# pprint(dict_id_ofensa)