import db
import tools_data
import tools_qradar

from models import Ticket
from pprint import pprint
from datetime import datetime, timedelta

import os
import re
import numpy as np


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
#                     "filter": "id=33099"
#                 }
#             )
# print(data_qradar, type(data_qradar))
# epoch = data_qradar[0]["start_time"]
# fecha_chl = tools_qradar.epoch2date_mili(epoch)
# print(fecha_chl)