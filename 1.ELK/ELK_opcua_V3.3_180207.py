import pandas as pd
#from scipy.stats import ttest_ind
from scipy.stats import ttest_ind
from elasticsearch import Elasticsearch
from pprint import pprint



def df_from_elastic_query(elastic_search_query):
    try:
        return pd.DataFrame.from_dict([item['_source'] for item in elastic_search_query['hits']['hits']])
    except:
        return pd.DataFrame()


es = Elasticsearch(
    ['10.101.100.178'],
    http_auth=('elastic','changeme'),
    port=9200
)

##################################################
###to query
pds=df_from_elastic_query(
        es.search(index="plc-*",
                doc_type="document",
                body={
                    "query": {
                    "range": {
                    ##query time
                    "timestamp": {
                            "gte": "2018-01-18T06:00:00",
                            "lte": "2018-01-18T12:00:00"
                                }
                            }
                        },
                    ##display size
                    "size": 5,
                    "_source": ["LSP", "timestamp", 'Dia_C_Xdisp', 'Dia_C_Ydisp']
                    }
                    ##size:actual size
                    ##head():display size
                    , size=30)).head(6)

print(pds)
print('\n')
print(pds.LSP)   #same as pds['LSP']
print('\n')
#print(pds[0:3])
#pds.to_csv(r'123.csv', sep='\t', encoding='utf-8')
pds.to_csv(r'/home/user/development/hello_python/1.ELK/ELK.csv')
pprint(ttest_ind(pds.Dia_C_Xdisp, pds.Dia_C_Ydisp))
