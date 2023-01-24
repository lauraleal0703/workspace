import os
import tools_data
import matplotlib.pyplot as plt

from pprint import pprint

from models import Ticket

os.system('clear')

customers = ["[AAN]",
    "Adaptive Security",
    "[BDO]",
    "[CAS]",
    "[EMSA]",
    "[EVERTEC]",
    "[SBPay]",
    "[SURA]",
    "[UDLA]",
    "[AS]",
    "[CMPC]",
    "[CCA]",
    "[CYT]",
    "[UDP]",
    "[UAI]",
    "[SINACOFI]"
]


start_date = "2018-01-01"
end_date = "2023-01-24"

tickets_customer_queue_6 = {}
tickets_customer_queue_6_year = {}
tickets_customer_queue_6_month = {}
tickets_customer_queue_6_day = {}
for customer in customers:
    tickets_queue = Ticket.tickets_by_queue_marca_date(6, customer, start_date , end_date)
    if customer not in tickets_customer_queue_6:
        tickets_customer_queue_6[customer] = {}
        tickets_customer_queue_6_year[customer] = {}
        tickets_customer_queue_6_month[customer] = {}
        tickets_customer_queue_6_day[customer] = {}
    
    for ticket in tickets_queue:
        year = ticket.create_time.strftime("%Y")
        month = ticket.create_time.strftime("%m")
        day =  ticket.create_time.strftime("%d")
        
        if year not in tickets_customer_queue_6[customer]:
            tickets_customer_queue_6[customer][year] = {}
            tickets_customer_queue_6_day[customer][year] = {}
            tickets_customer_queue_6_month[customer][year] = {}
            tickets_customer_queue_6_year[customer][year] = 1
        else:
            tickets_customer_queue_6_year[customer][year] += 1
        
        if int(month) not in tickets_customer_queue_6[customer][year]:
            tickets_customer_queue_6[customer][year][int(month)] = {}
            tickets_customer_queue_6_day[customer][year][int(month)] = {}
            tickets_customer_queue_6_month[customer][year][int(month)] = 1
        else:
            tickets_customer_queue_6_month[customer][year][int(month)] += 1

        if int(day) not in tickets_customer_queue_6[customer][year][int(month)]:
            tickets_customer_queue_6[customer][year][int(month)][int(day)] = [ticket.id]
            tickets_customer_queue_6_day[customer][year][int(month)][int(day)] = 1
        else:
            tickets_customer_queue_6[customer][year][int(month)][int(day)].append(ticket.id)
            tickets_customer_queue_6_day[customer][year][int(month)][int(day)] += 1

# pprint(tickets_customer_queue_6.keys())
# pprint(tickets_customer_queue_6_year["[SBPay]"])
# pprint(tickets_customer_queue_6_month["[SBPay]"])
# print(tickets_customer_queue_6_day["[SBPay]"])

tools_data.save_data_json(f"tickets_customer_queue_6", tickets_customer_queue_6)
tools_data.save_data_json(f"tickets_customer_queue_6_year", tickets_customer_queue_6_year)
tools_data.save_data_json(f"tickets_customer_queue_6_month", tickets_customer_queue_6_month)
tools_data.save_data_json(f"tickets_customer_queue_6_day", tickets_customer_queue_6_day)


customers = ["[AAN]",
    "Adaptive Security",
    "[BDO]",
    "[CAS]",
    "[EMSA]",
    "[EVERTEC]",
    "[SBPay]",
    "[SURA]",
    "[UDLA]",
    "[AS]",
    "[CMPC]",
    "[CCA]",
    "[CYT]",
    "[UDP]",
    "[UAI]",
    "[SINACOFI]"
]

customers = ["[AAN]",
    "[BDO]",
    "[CAS]",
    "[EMSA]",
    "[SURA]",
    "[UDLA]"
]

customers = ["Adaptive Security"]

x_eje = []
for customer in customers:
    datos = tickets_customer_queue_6_year[customer]
    x = []
    y = []
    for year in sorted(tickets_customer_queue_6_year[customer]):
        if year not in x_eje:
            x_eje.append(int(year))
        x.append(int(year))
        y.append(tickets_customer_queue_6_year[customer][year])

    plt.plot(x, y, label=f"{customer} =  {sum(y)}")
    plt.xticks(x_eje, x_eje, fontsize=8)
    plt.yticks(fontsize=8)
    plt.legend(loc="upper left", fontsize=8)
    plt.tick_params(axis="both", which="both", labelsize=8)
    plt.title(f"Requerimientos de Clientes", fontsize=8)
plt.grid()
plt.savefig(f"graphs/customers_year_adaptive.png", dpi=300, bbox_inches='tight')

