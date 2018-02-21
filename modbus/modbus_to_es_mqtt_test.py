import csv
import math
import struct
import json
from datetime import datetime, date
from time import sleep
from collections import OrderedDict

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ConnectionException

from elasticsearch import Elasticsearch
from elasticsearch import helpers

import paho.mqtt.client as mqtt

def decimals_to_float32(int1, int2):
    """Convert to float
    
    Note:
        Orders in big endian
    Args:
        int1, int2 (int)
    Return:
        float: decoded value
    """
    f = int('{:016b}{:016b}'.format(int1, int2), 2)
    return struct.unpack('f', struct.pack('I', f))[0]


def unpack_bool(data):
    """Extract list of boolean from integer
    
    Args:
        data (int)
    Return:
        list: in bool
    """
    return [bool(int(i)) for i in '{:016b}'.format(data)]


def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val


def csv_to_dict(tag_csv):
    """ create a parsing dictionary """
    #have order dictionary, original dic is hash that not  order
    tags = OrderedDict()
    with open(tag_csv, 'r') as f:
        reader = csv.reader(f, doublequote=True, quoting=csv.QUOTE_ALL, escapechar='\\')
        header = next(reader)
        header[0] = 'Name' # manually adjust from \ufeffName to Name
        tags = {row[0]:{header[i]:row[i] for i in range(0,len(header))} for row in reader}
    return tags


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


# -----

def insert_data(tags, data):
    """ process from a list of data and insert to its tags accordingly 
    
    TODO: Word datatype parsing
    """
    data_iter = iter(data)
    for tag in tags:
        val = next(data_iter)
        if tags[tag]["Data Type"] == "Real":
            val = decimals_to_float32(val, next(data_iter))
        elif tags[tag]["Data Type"] == "Word":
            pass
        elif tags[tag]["Data Type"] == "Int":
            val = twos_comp(val, 16)
        if tags[tag]['scale'] == 'x10':
            val /= 10
        tags[tag]['value'] = val

    return tags


# load file
tags = csv_to_dict('plc_tags.csv')
#connect Modbus
mb = ModbusTcpClient('192.168.11.150', port=502, retries=3, timeout=3)
mb.connect()
#connect ELK
es = Elasticsearch()
#connect MQTT
mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)
#connect settime
time = datetime.now()

while True:
    try:
        # Read Modbus (ID address,byte of count, MOdbus slave ID)
        rr = mb.read_holding_registers(address=0,count=103,unit=1)
        assert(rr.function_code < 0x80), "register error"

        tags = insert_data(tags, rr.registers)
        formatted_data = {tag:tags[tag]['value'] for tag in tags if tags[tag]['Data Type'] != "Word"}
        formatted_data["timestamp"] = datetime.utcnow()
        actions = {
            "_index": "plc-{}".format(datetime.now().strftime("%Y.%m.%d")),
            "_type": "document",
            "_id": hash(datetime.now()),
            "_source": json.dumps(formatted_data, default=json_serial)
        }
        
        mqttc.publish("aspm1188/data", json.dumps(actions, sort_keys=True, indent=4))

        print("Indexed at {}".format(datetime.now().strftime('%c')))
        helpers.bulk(es, [actions])

    except ConnectionException:
        print('Error: Connection error')

    except KeyboardInterrupt:
        print('Warning: Interrupted')
        raise

    sleep(1)
    
mb.close()
