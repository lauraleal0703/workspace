import tools_qradar
from pprint import pprint


"""
data = tools_qradar.login_attempts(
        headers={"Range": "items=0-5"},
        params={
            "fields":"attempt_time",
            "filter": "attempt_result='SUCCESS'",
            "sort":"-attempt_time"
            }
        )

for pos, dato in enumerate(data):
    epoch = dato["attempt_time"]
    fecha_chl = tools_qradar.epoch2date(epoch)
    print(pos, fecha_chl)
"""

# data_0 = tools_qradar.rules(headers={"Range": "items=0-1"})
data_1 = tools_qradar.offenses(
    headers={"Range": "items=0-10"}, 
    params={
        "fields":"id",
        "sort":"-id"
    }
    )

# data_2 = tools_qradar.domain_management_domains(headers={"Range": "items=0-1"})
# data_3 = tools_qradar.offense_types(headers={"Range": "items=0-1"})
# data_4 = tools_qradar.ariel_searches(headers={"Range": "items=0-1"})

# data_error = tools_qradar.curl_general("https://172.16.17.10/api/reference_data/sets/test_set")


pprint(data_1)