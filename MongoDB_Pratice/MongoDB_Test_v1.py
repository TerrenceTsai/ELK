from pymongo import MongoClient
import json
from pymongo import errors
from bson import json_util
from datetime import datetime, date
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
conn = MongoClient('0.0.0.0',27017)
#db=client.admin
# Issue the serverStatus command and print the results
#creat elasticDB
db=conn.elasticdb
print(dir(errors))

#elastic
from elasticsearch import Elasticsearch
es = Elasticsearch(
    http_auth=('elastic','changeme')
)
#Data structure
#
post = es.search(index="plc-*",
                doc_type="document",
                body={
                    "query": {
                        "range": {
                            "timestamp": {
                                "gte": "2018-01-18T06:00:00",
                                "lte": "2018-01-18T12:00:00"
                            }
                        }
                    },
                    "size":0,
                    "aggs":{
                    "Std_self": {
                        "extended_stats": {
                            "field": "Dia_C_Ydisp",
                            "missing": 0
                        }
                      }
                    }
                   }
                )
print('%d document found'% post['hits']['total'])
#jason_loads=json.dumps(res,indent=4)
#print(json.dumps(res,indent=4))
#print(json.loads(jason_loads))
"""post=[
    {'name':'Andy',"address":'Taiper',"age":25,"timestamp":"datetime.utcnow()"},
    {'name': 'Andy', "address": 'Taiper', "age": 25,"timestamp":"datetime.utcnow()"},
    {'name': 'Andy', "address": 'Taiper', "age": 25,"timestamp":"datetime.utcnow()"}
]
"""
#covert JSON to BSON(mongDB-specific prefer
print(type(post_json))
post_json=json.dumps(post,indent=4)
post_json_bson=json_util.loads(post_json)
object_id=db.col.insert(post_json_bson)
print(db.col.find_one())


#db.col.insert({"name":'Terrence','province':'Taipei','age':25})
import datetime
