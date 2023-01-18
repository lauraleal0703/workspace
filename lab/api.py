import tools_qradar
from pprint import pprint


######################
#--------Fields-------
#######################

"""'
last_persisted_time', 'username_count', 'description', 'rules', 
'event_count', 'flow_count', 'assigned_to', 'security_category_count',
 'follow_up', 'source_address_ids', 'source_count', 'inactive', 
 'protected', 'closing_user', 'destination_networks', 'source_network', 
 'category_count', 'close_time', 'remote_destination_count', 
 'start_time', 'magnitude', 'last_updated_time', 'credibility', 'id', 
 'categories', 'severity', 'policy_category_count', 'log_sources', 
 'closing_reason_id', 'device_count', 'first_persisted_time', 
 'offense_type', 'relevance', 'domain_id', 'offense_source', 
 'local_destination_address_ids', 'local_destination_count', 'status'])
"""

######################
#--------Data-------
#######################
print("hola")
print("hola")


data = tools_qradar.offenses(
        headers={"Range": "items=0-3"}, 
        params={
                "fields": "id"
                }
        )

pprint(data)

# data = tools_qradar.offenses(
#         headers={"Range": "items=0-5"}, 
#         params={
#                 "fields": "id,description,start_time,log_sources",
#                 "filter": "id=59439",
#                 "sort":"+start_time"
#                 }
#         )

# pprint(data)

# dict_offenses = {}
# for dato in data:
#     for params in dato:
#         if params not in dict_offenses:
#             dict_offenses[params] = [dato[params]]
#         else:
#             dict_offenses[params].append(dato[params])

# dict_offenses["dateChl"] = []
# for epoch in dict_offenses["start_time"]:
#     fecha_chl = tools_qradar.epoch2date(epoch)
#     dict_offenses["dateChl"].append(fecha_chl)
# dict_offenses.pop('start_time')

# pprint(dict_offenses)