import pymongo
import datetime
import time
from pymongo import MongoClient

#Connecting to the cluster
cluster =MongoClient(<code/credentials to connect to the mongodb remote server>)

#Specifying which DB
db=cluster['Dummy']    

#Specifying which collection in the DB
collection=db['dummy_collection'] 

# a job scheduled to run every 10 seconds
while(True):
    ob=collection.insert_one({'Message':"Scheduler code.py","Time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    print("------------------------ Added at : "+time.ctime()+"------------------------")
    time.sleep(10)  # 10 seconds.
    print(ob.inserted_id)  #to print the id of the records added in the collection(for debugging, this value can be observed in the heroku logs)

