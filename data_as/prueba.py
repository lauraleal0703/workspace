import db
import tools_data
import tools_qradar

from models import Ticket, Users, TicketHistory
from pprint import pprint
from datetime import datetime, timedelta

import os
import json
import re
import numpy as np

os.system('clear')
inicio = datetime.now()

user = Users.get(50)

# print(">>---------Prueba personalizada---------------")

# data_otrs = db.session.query(Ticket).filter(Ticket.id == 38762).first()
ticket = Ticket.get(38762)
print(f"ticket {ticket}")

tickets = Ticket.tickets_by_offense("61870")
print(f"ticket {tickets}")
for ticket in tickets:
    print(ticket.tn, ticket.create_time, ticket.change_time, ticket.last_history.change_time)
    for last_ in ticket.ticket_history:
        print(last_.change_time)


# print(user.full_name)
# for ticket in user.tickets:
#     print(ticket.tn, ticket.create_time, ticket.change_time, ticket.last_history)


# data_otrs = db.session.query(Ticket).filter(Ticket.title.like("61817%")).all()
# print(data_otrs.title)
# print(set(re.findall(r"\d{5,}|-|\d{5,}", data_otrs.title)))
# print(len(re.findall(r"\d{5,}|-|\d{5,}", data_otrs.title)))
# exit()


# print(data_otrs.title)
# print(data_otrs.create_time)

# data_qradar = tools_qradar.offenses(
#                 params={
#                     "fields": "start_time",
#                     "filter": "id=33099"
#                 }
#             )
# print(data_qradar, type(data_qradar))
# epoch = data_qradar[0]["start_time"]
# fecha_chl = tools_qradar.epoch2date_mili(epoch)
# print(fecha_chl)


# print(">>---------Prueba personalizada---------------")

# # data_otrs = db.session.query(Users).filter(Users.id == 67).first()
# # print(data_otrs.first_name)

# customers = ["AAN",
#     "Adaptive Security",
#     "BDO",
#     "CAS",
#     "EMSA",
#     "EVERTEC",
#     "Evertec",
#     "SBPay",
#     "SBPAY",
#     "SURA",
#     "UDLA",
#     "AS",
#     "CMPC",
#     "CCA",
#     "CYT",
#     "UDP",
#     "UAI",
#     "SINACOFI",
#     "Fwd",
#     "Re:",
#     "RE:",
#     "RV:"
# ]

# data_otrs = db.session.query(Ticket).filter(Ticket.queue_id == 6, Ticket.create_time >= "2023-01-01").all()
# # data_otrs = db.session.query(Ticket).filter(Ticket.title.like("61817%")).all()
# for dato in data_otrs:
#     print(dato.id)
#     data_history = db.session.query(TicketHistory).filter(TicketHistory.ticket_id == dato.id).all()
#     tiempos = []
#     for history in data_history:
#         print(history.change_time)
#         tiempos.append(history.change_time)
#     print(max(tiempos.set()))
    

# path_ticket_offenses_year = os.path.join("data_collected", "ticket_offenses_year_2022.json")
# ticket_offenses_year = open(path_ticket_offenses_year)
# ticket_offenses_year = json.load(ticket_offenses_year)
# pprint(ticket_offenses_year["12"]["28"]["automatic"]["fails"])