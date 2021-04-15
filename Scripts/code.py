import pymongo
import datetime
import time
from connection import str_val
from pymongo import MongoClient

#Connecting to the cluster
cluster =MongoClient(str_val)
print(str_val)

#Specifying which DB
db=cluster['Dummy']    

#Specifying which collection in the DB
collection=db['dummy_collection'] 


while(True):
    ob=collection.insert_one({'Message':"Scheduler code.py","Time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    print("------------------------ Added at : "+time.ctime()+"------------------------")
    time.sleep(10)  # 10 seconds.
    print(ob.inserted_id)

