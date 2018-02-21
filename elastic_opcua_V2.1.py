from time import sleep
import json
from datetime import datetime

from opcua import Client
from opcua import ua

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import os

es = Elasticsearch(
    http_auth=('elastic','changeme')
)

client = Client("opc.tcp://10.101.100.39:4840")

parent_names = {
    'energy': 'ns=3;s="Data_From_Energy_PLC_DB"."DS142"',
    'fishtank': 'ns=3;s="Data_From_Fish_PLC_DB".Static',
    'security': 'ns=3;s="Data_From_Security_DB".Static'
}

connected = False

while True:
    try:
        client.connect()
        connected = True
        
        parents = {}
        data = {}
        for name in parent_names:
            parents[name] = client.get_node(parent_names[name])
            data[name] = {}

        while True:
            for parent in parents:
                data[parent]["timestamp"] = datetime.utcnow()                
                for child in parents[parent].get_children():
                    data[parent][child.get_browse_name().Name] = child.get_value()


            # actions = [
            #     {
            #         "_index": "python-opcua",
            #         "_type": stuff,
            #         "_source": data[stuff]
            #     }
            #     for stuff in data
            # ]
            # print(actions)
            # helpers.bulk(es, actions)

            for stuff in data:
                # plc-fishtank-2017.08.03
                index_str = 'plc-' + stuff + '-' + datetime.now().strftime('%Y.%m.%d')
                es.index(index=index_str,
                         doc_type='plc',
                         body=data[stuff]
                )
                print(datetime.now().strftime('%c'), "Data indexed : ", index_str)

            sleep(5)

    except:
        if connected:
#            client.disconnect()
            print("Disconnected")
            
        connected = False
        sleep(1)
    print(datetime.now().strftime('%c'), "Waiting for connection, script restarting")
    sleep(1)

hostname = "10.0.2.15"
response = os.system("ping -c 1 " + hostname)
# and then check the response...
if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "Network Error"
print(pingstatus)
print(pingstatus)