import db
import tools_data
import tools_qradar

from models import Ticket
from pprint import pprint
from datetime import datetime, timedelta

import os
import re
import json

os.system('clear')


# print(">>---------Prueba personalizada---------------")

# data_otrs = db.session.query(Ticket).filter(Ticket.tn == 2022123154000438).first()
# print(data_otrs.title)
# print(data_otrs.create_time)

# data_qradar = tools_qradar.offenses(
#                 params={
#                     "fields": "start_time",
#                     "filter": f"id=64749"
#                     }
#                 )
# epoch = data_qradar[0]["start_time"]
# fecha_chl = tools_qradar.epoch2date_mili(epoch)
# print(fecha_chl)
# exit()


print(">>---------OTRS-->-----QRadar---------")

data_otrs = db.session.query(Ticket).filter(
                Ticket.create_time>="2022-12-01",
                Ticket.create_time<"2022-12-31 23:00:00")

dict_id_offenses_handwork_low_successes = {}
dict_id_offenses_handwork_low_fails = {}
dict_id_offenses_handwork_mean_successes = {}
dict_id_offenses_handwork_mean_fails = {}
dict_id_offenses_handwork_high_successes = {}
dict_id_offenses_handwork_high_fails = {}
dict_id_offenses_automatic_low_successes = {}
dict_id_offenses_automatic_low_fails = {}
dict_id_offenses_automatic_mean_successes = {}
dict_id_offenses_automatic_mean_fails = {}
dict_id_offenses_automatic_high_successes = {}
dict_id_offenses_automatic_high_fails = {}
dict_offenses_indefinidas = {}

for ticket in data_otrs:
    if len(re.findall(r"Ofensa", ticket.title)) > 0 and len(re.findall(r"\d{5,}", ticket.title)) > 0 and not len(re.findall(r"\d{5,}-\d{5,}", ticket.title)) > 0:
        id_offense = re.findall(r"\d{5,}", ticket.title)
        data_qradar = tools_qradar.start_time_offenses(id_offense[0])
        if data_qradar:
            start_time_qradar = datetime.fromtimestamp(data_qradar)
            create_time_otrs = ticket.create_time + timedelta(hours=1)
            response_time = create_time_otrs - start_time_qradar
            ideal_response_time = timedelta(minutes=15)
            handwork = re.findall(r"Ofensa N°", ticket.title)
            if handwork:
                if len(re.findall(r"Criticidad|Baja", ticket.title)) > 1:
                    if response_time <= ideal_response_time:
                        dict_id_offenses_handwork_low_successes[ticket.tn] = {"id_qradar": id_offense[0],
                                                                                "id_otrs": ticket.id,
                                                                                "start_time": start_time_qradar,
                                                                                "create_time":create_time_otrs,
                                                                                "response_time": response_time
                                                                                }
                    else:
                        dict_id_offenses_handwork_low_fails[ticket.tn] = {"id_qradar": id_offense[0],
                                                                            "id_otrs": ticket.id,
                                                                            "start_time": start_time_qradar,
                                                                            "create_time":create_time_otrs,
                                                                            "response_time": response_time
                                                                            }
                elif len(re.findall(r"Criticidad|Media", ticket.title)) > 1:
                    if response_time <= ideal_response_time:
                        dict_id_offenses_handwork_mean_successes[ticket.tn] = {"id_qradar": id_offense[0],
                                                                                "id_otrs": ticket.id,
                                                                                "start_time": start_time_qradar,
                                                                                "create_time":create_time_otrs,
                                                                                "response_time": response_time
                                                                                }
                    else:
                        dict_id_offenses_handwork_mean_fails[ticket.tn] = {"id_qradar": id_offense[0],
                                                                            "id_otrs": ticket.id,
                                                                            "start_time": start_time_qradar,
                                                                            "create_time":create_time_otrs,
                                                                            "response_time": response_time
                                                                            }
                elif len(re.findall(r"Criticidad|Alta", ticket.title)) > 1:
                    if response_time <= ideal_response_time:
                        dict_id_offenses_handwork_high_successes[ticket.tn] = {"id_qradar": id_offense[0],
                                                                                "id_otrs": ticket.id,
                                                                                "start_time": start_time_qradar,
                                                                                "create_time":create_time_otrs,
                                                                                "response_time": response_time
                                                                                }
                    else:
                        dict_id_offenses_handwork_high_fails[ticket.tn] = {"id_qradar": id_offense[0],
                                                                            "id_otrs": ticket.id,
                                                                            "start_time": start_time_qradar,
                                                                            "create_time":create_time_otrs,
                                                                            "response_time": response_time
                                                                            }
                else:
                    print(f"---Alerta Manual {ticket.tn} {ticket.title}")
            else:
                if len(re.findall(r"Criticidad|Baja", ticket.title)) > 1:
                    if response_time <= ideal_response_time:
                        dict_id_offenses_automatic_low_successes[ticket.tn] = {"id_qradar": id_offense[0],
                                                                                "id_otrs": ticket.id,
                                                                                "start_time": start_time_qradar,
                                                                                "create_time":create_time_otrs,
                                                                                "response_time": response_time
                                                                                }
                    else:
                        dict_id_offenses_automatic_low_fails[ticket.tn] = {"id_qradar": id_offense[0],
                                                                            "id_otrs": ticket.id,
                                                                            "start_time": start_time_qradar,
                                                                            "create_time":create_time_otrs,
                                                                            "response_time": response_time
                                                                            }
                elif len(re.findall(r"Criticidad|Media", ticket.title)) > 1:
                    if response_time <= ideal_response_time:
                        dict_id_offenses_automatic_mean_successes[ticket.tn] = {"id_qradar": id_offense[0],
                                                                                "id_otrs": ticket.id,
                                                                                "start_time": start_time_qradar,
                                                                                "create_time":create_time_otrs,
                                                                                "response_time": response_time
                                                                                }
                    else:
                        dict_id_offenses_automatic_mean_fails[ticket.tn] = {"id_qradar": id_offense[0],
                                                                            "id_otrs": ticket.id,
                                                                            "start_time": start_time_qradar,
                                                                            "create_time":create_time_otrs,
                                                                            "response_time": response_time
                                                                            }
                elif len(re.findall(r"Criticidad|Alta", ticket.title)) > 1:
                    if response_time <= ideal_response_time:
                        dict_id_offenses_automatic_high_successes[ticket.tn] = {"id_qradar": id_offense[0],
                                                                                "id_otrs": ticket.id,
                                                                                "start_time": start_time_qradar,
                                                                                "create_time":create_time_otrs,
                                                                                "response_time": response_time
                                                                                }
                    else:
                        dict_id_offenses_automatic_high_fails[ticket.tn] = {"id_qradar": id_offense[0],
                                                                            "id_otrs": ticket.id,
                                                                            "start_time": start_time_qradar,
                                                                            "create_time":create_time_otrs,
                                                                            "response_time": response_time
                                                                            }
                else:
                    print(f"---Alerta Automatica {ticket.tn} {ticket.title}")
        else:
            dict_offenses_indefinidas[ticket.tn] = {"id": ticket.id,
                                                    "title": ticket.title,
                                                    "star_time": ticket.create_time
                                                    }
    else:
        dict_offenses_indefinidas[ticket.tn] = {"id": ticket.id,
                                                "title": ticket.title,
                                                "star_time": ticket.create_time
                                                }


datos_graficar = {"offenses_handwork_low_successes": 
                    [len(dict_id_offenses_handwork_low_successes), dict_id_offenses_automatic_low_successes.keys()],
                "offenses_handwork_low_fails":
                    [len(dict_id_offenses_handwork_low_fails), dict_id_offenses_handwork_low_fails.keys()],
                "offenses_automatic_low_successes":
                    [len(dict_id_offenses_automatic_low_successes), dict_id_offenses_automatic_low_successes.keys()],
                "offenses_automatic_low_fails":
                    [len(dict_id_offenses_automatic_low_fails), dict_id_offenses_automatic_low_fails.keys()],
                "offenses_handwork_mean_successes":
                    [len(dict_id_offenses_handwork_mean_successes), dict_id_offenses_handwork_mean_successes.keys()],
                "offenses_handwork_mean_fails":
                    [len(dict_id_offenses_handwork_mean_fails), dict_id_offenses_handwork_mean_fails.keys()],
                "offenses_automatic_mean_successes":
                    [len(dict_id_offenses_automatic_mean_successes), dict_id_offenses_automatic_mean_successes.keys()],
                "offenses_automatic_mean_fails":
                    [len(dict_id_offenses_automatic_mean_fails), dict_id_offenses_automatic_mean_fails.keys()],
                "offenses_handwork_high_successes":
                    [len(dict_id_offenses_handwork_high_successes), dict_id_offenses_handwork_high_successes.keys()],
                "offenses_handwork_high_fails":
                    [len(dict_id_offenses_handwork_high_fails), dict_id_offenses_handwork_high_fails.keys()],
                "offenses_automatic_high_successes":
                    [len(dict_id_offenses_automatic_high_successes), dict_id_offenses_automatic_high_successes.keys()],
                "offenses_automatic_high_fails":
                    [len(dict_id_offenses_automatic_high_fails), dict_id_offenses_automatic_high_fails.keys()],
                "offenses_indefinidas":
                    [len(dict_offenses_indefinidas), dict_offenses_indefinidas.keys()]
                }

pprint(datos_graficar)

# json_object = json.dumps(datos_graficar)


# print(total_offenses_handwork_successes) #189
# print(total_offenses_handwork_fails) # 446
# print(total_offenses_handwork) #635
# print(total_offenses_automatic_successes)
# print(total_offenses_automatic_fails)
# print(total_offenses_automatic)
# print(total_offenses_indefinidas)