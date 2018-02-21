from time import sleep
import json
from datetime import datetime
from opcua import Client
from pprint import pprint

from elasticsearch import Elasticsearch


def df_from_elastic_query(elastic_search_query):
    try:
        return pd.DataFrame.from_dict([item['_source'] for item in elastic_search_query['hits']['hits']])
    except:
        return pd.DataFrame()


es = Elasticsearch(
    http_auth=('elastic','changeme')
)

res = es.search(index="plc-*",
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
                    "size":5,
                    "aggs":{
                    "Std_self": {
                        "extended_stats": {
                            "field": "Dia_C_Ydisp",
                            "missing": 0
                        }
                      }
                    },
                    "_source":["LSP"]
                   }
                )

pprint(res.values())
# res is json style
print('%d document found'% res['hits']['total'])
print(res['aggregations']['Std_self']['avg'])
for tag in res['hits']['hits']:
    print(tag['_id'], tag['_source']['LSP'])

#pprint(res['aggregations']['Std_self']['avg'])
pprint(res)
pprint(type(res))

