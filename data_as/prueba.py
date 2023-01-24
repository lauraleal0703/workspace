import db
import tools_data
import tools_qradar

from models import Ticket
from models import User
from models import TicketHistory
from models import TicketPriority
from models import TicketState

from pprint import pprint
from datetime import datetime, timedelta

import os
import json
import re
import numpy as np

os.system('clear')
# inicio = datetime.now()


# data = Ticket.get_by_tn(2023010354000189)
# print(data.title)
# print(data.id)
# ticket = TicketHistory.get(39794)
# for moment in ticket:
#     print(f"\nid  = {moment.id}")
#     print(f"name = {moment.name}")
#     print(f"Creation = {moment.create_time}")
#     print(f"priority = {moment.priority.name}")
#     print(f"history_type = {moment.ticket_history_type.name}")
#     print(f"Tipo = {moment.ticket_type.name}")
#     print(f"State = {moment.ticket_state.name}")
#     print(f"ClasState = {moment.ticket_state.type_state.name}")

start_date = "2023-01-01"
end_date = "2023-01-10"
tickets_period = Ticket.tickets_by_date(start_date , end_date)
tickets_cola = Ticket.tickets_by_queue_date(6, start_date , end_date)
# for ticket in tickets:
#     ticket_history = TicketHistory.get(ticket.id)
#     types_id = []
#     for moment in ticket_history:
#         types_id.append(moment.type_id)
    
#     if 68 not in types_id:
#         print(f"\nNuevo Ticket -- {ticket.id} -- Responsable: {ticket.user.full_name}")
#         data = Ticket.get_by_tn(ticket.tn)
#         print(f"Title: {data.title}")
#         resolution_time = ticket.change_time - ticket.create_time
#         print(f"Tiempo de resolución {resolution_time}"

user_id = 53
user = User.get(user_id)
print(f"Responsable: {user.full_name}")
tickets_user = Ticket.tickets_by_user_date(user_id, start_date, end_date) 
tickets_user_cola = Ticket.tickets_by_queue_user_date(6, user_id, start_date, end_date)
for ticket in tickets_user_cola:
    ticket_history = TicketHistory.get(ticket.id)
    types_id = []
    for moment in ticket_history:
        types_id.append(moment.type_id)
    
    if 68 not in types_id:
        print(f"\nNuevo Ticket -- {ticket.id}")
        data = Ticket.get_by_tn(ticket.tn)
        print(f"Title: {data.title}")
        resolution_time = ticket.change_time - ticket.create_time
        print(f"Tiempo de resolución {resolution_time}")
    else:
        print(f"\nNuevo Ticket -- {ticket.id} -- Title: {data.title}")
        print("Sin SLA")


print(f"\nTotal tickets_period {len(tickets_period)}")
print(f"Total tickets_adm {len(tickets_cola)}")
print(f"Total tickets_user {len(tickets_user)}")
print(f"Total tickets_user_cola {len(tickets_user_cola)}")


# users_queue_9_name = [(53, 'Solange Aravena H.'), 
#     (59, 'Miguel González M.'), 
#     (29, 'Francisco Sepulveda'), 
#     (52, 'Miguel Almendra V.'), 
#     (47, 'Andrés Rojas'), 
#     (63, 'Diego Orellana V.'), 
#     (12, 'Jose Nicolas'), 
#     (65, 'Nicolas Garrido'), 
#     (58, 'Dorian Malfert M.'), 
#     (1, 'Admin OTRS'), 
#     (54, 'Cristopher Ulloa'), 
#     (56, 'Sugy Nam'), 
#     (64, 'Mauricio Retamales'), 
#     (45, 'Jonathan Finschi')
# ]
# users_queue_9 = [53, 59, 29, 52, 47, 63, 12, 65, 58, 1, 54, 56, 64, 45]

# user = User.get(52)
# print(user.full_name)
# for ticket in user.tickets:
#     resolution_time = ticket.change_time - ticket.create_time
#     print(f"\nTicket ID = {ticket.id} {ticket.title}")
#     print(f"Tiempo de resolución {resolution_time}")
#     ticket_history = TicketHistory.get(ticket.id)
#     for moment in ticket_history:
#         print(f"\nid  = {moment.id}")
#         print(f"name = {moment.name}")
#         print(f"Start = {moment.create_time} End = {moment.ticket.last_history}")
#         print(f"priority = {moment.priority.name}")
#         print(f"history_type = {moment.ticket_history_type.name}")
#         print(f"Tipo = {moment.ticket_type.name}")
#         print(f"State = {moment.ticket_state.name}")
#         print(f"ClasState = {moment.ticket_state.type_state.name}")


# print("Prioridad")
# data_1 = TicketPriority.all()
# for da in data_1:
#     print(f"id={da.id} - {da.name}")

# print("Estados")
# data_2 = TicketState.all()
# for da in data_2:
#     print(f"id={da.id} - {da.name}")

# exit()

# user = User.get(50)

# users = User.all()
# for user in users:
#     user.f

# # print(">>---------Prueba personalizada---------------")

# # data_otrs = db.session.query(Ticket).filter(Ticket.id == 38762).first()
# ticket = Ticket.get(38762)
# print(f"ticket {ticket}")
# ticket.t

# tickets = Ticket.tickets_by_offense("61870")


# print(f"ticket {tickets}")
# for ticket in tickets:
#     print(ticket.tn, ticket.create_time, ticket.change_time, ticket.last_history.change_time)
#     for last_ in ticket.ticket_history:
#         print(last_.change_time)


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