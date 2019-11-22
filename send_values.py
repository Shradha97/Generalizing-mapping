from __future__ import division
from ubidots import ApiClient
import datetime

def make_devices(m):
    #apilist = []
    data_sources = []
    new_variable1 = []
    new_variable2 = []
    new_variable3 = []
    new_variable4 = []
    for i in range(m):
        api = ApiClient(token = 'BBFF-vwaOtO0NBWQL7oqbg7I4GAIRUs91Bo')
        #apilist.append(ApiClient(token = 'BBFF-vwaOtO0NBWQL7oqbg7I4GAIRUs91Bo'))

        #new_datasource = api.create_datasource({"name": "Health_status", "description": "Has health parameters that can depict the health status"})
        data_sources.append(api.create_datasource({"name": "Health_status", "description": "Has health parameters that can depict the health status"}))

        new_variable1.append(data_sources[i].create_variable({"name": "Temperature score", "unit": "unitless"}))
        new_variable2.append(data_sources[i].create_variable({"name": "Heart Rate score", "unit": "unitless"}))
        new_variable3.append(data_sources[i].create_variable({"name": "Blood Pressure score", "unit": "unitless"}))
        new_variable4.append(data_sources[i].create_variable({"name": "Health score", "unit": "unitless"}))
    return new_variable1, new_variable2, new_variable3, new_variable4, data_sources


def totimestamp(dt, epoch):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6

def get_timestamp():
    dt = datetime.datetime.now().timestamp()
    #timestamp = totimestamp(dt, datetime.datetime(1970,1,1))
    return int(dt) #int(timestamp)

def values(t, hr, bp, new_variable1, new_variable2, new_variable3, new_variable4, ds, hs):
    timestamp = get_timestamp()
    new_variable1.save_values([{'timestamp': timestamp, 'value': t}])
    new_variable2.save_values([{'timestamp': timestamp, 'value': hr}])
    new_variable3.save_values([{'timestamp': timestamp, 'value': bp}])
    new_variable4.save_values([{'timestamp': timestamp, 'value': hs}])
