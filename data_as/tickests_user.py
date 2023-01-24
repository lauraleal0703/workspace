import os
import tools_data

from pprint import pprint

from models import Ticket
from models import User

os.system('clear')

start_date = "2018-01-01"
end_date = "2023-01-24"
tickets_queue = Ticket.tickets_by_queue_date(6, start_date , end_date)
tickets_user_queue_6 = {}
tickets_user_queue_6_year = {}
tickets_user_queue_6_month = {}
tickets_user_queue_6_day = {}
for ticket in tickets_queue:
    year = ticket.create_time.strftime("%Y")
    month = ticket.create_time.strftime("%m")
    day =  ticket.create_time.strftime("%d")
    if ticket.user_id not in tickets_user_queue_6:
        tickets_user_queue_6[ticket.user_id] = {}
        tickets_user_queue_6_year[ticket.user_id] = {}
        tickets_user_queue_6_month[ticket.user_id] = {}
        tickets_user_queue_6_day[ticket.user_id] = {}
    
    if year not in tickets_user_queue_6[ticket.user_id]:
        tickets_user_queue_6[ticket.user_id][year] = {}
        tickets_user_queue_6_day[ticket.user_id][year] = {}
        tickets_user_queue_6_month[ticket.user_id][year] = {}
        tickets_user_queue_6_year[ticket.user_id][year] = 1
    else:
        tickets_user_queue_6_year[ticket.user_id][year] += 1
    
    if int(month) not in tickets_user_queue_6[ticket.user_id][year]:
        tickets_user_queue_6[ticket.user_id][year][int(month)] = {}
        tickets_user_queue_6_day[ticket.user_id][year][int(month)] = {}
        tickets_user_queue_6_month[ticket.user_id][year][int(month)] = 1
    else:
        tickets_user_queue_6_month[ticket.user_id][year][int(month)] += 1

    if int(day) not in tickets_user_queue_6[ticket.user_id][year][int(month)]:
        tickets_user_queue_6[ticket.user_id][year][int(month)][int(day)] = [ticket.id]
        tickets_user_queue_6_day[ticket.user_id][year][int(month)][int(day)] = 1
    else:
        tickets_user_queue_6[ticket.user_id][year][int(month)][int(day)].append(ticket.id)
        tickets_user_queue_6_day[ticket.user_id][year][int(month)][int(day)] += 1

# pprint(tickets_user_queue_6.keys())
# pprint(tickets_user_queue_6_year[52])
# pprint(tickets_user_queue_6_month[52])
# print(tickets_user_queue_6_day[52])


tools_data.save_data_json(f"tickets_user_queue_6", tickets_user_queue_6)
tools_data.save_data_json(f"tickets_user_queue_6_year", tickets_user_queue_6_year)
tools_data.save_data_json(f"tickets_user_queue_6_month", tickets_user_queue_6_month)
tools_data.save_data_json(f"tickets_user_queue_6_day", tickets_user_queue_6_day)

x = []
for user_id in tickets_user_queue_6_year.keys():
    user = User.get(user_id)

    print(user)

'''
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
''' 
