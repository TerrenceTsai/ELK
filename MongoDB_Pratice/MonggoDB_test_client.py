from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
conn = MongoClient('10.101.100.178', 27017)
db=conn.elasticdb
print(db.elasticdb_collection)
array= db.col_collection.find_one()
print(array)
#for doc in array:
#    print(doc)