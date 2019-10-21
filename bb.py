import json
import pymongo
from pprint import pprint

#running the task file

with open(r'C:\Users\Joe Rishwanth\Desktop\task_map.json') as f:
 task_map = json.load(f)
task=task_map['taskInfo']
print(task)



#setting a mongoclient

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
mydbaaa = client.databaasyy

#inserting the collection

mydbaaa.mycol1.insert_many(task)
print(mydbaaa.list_collection_names())
firstcoll = mydbaaa.mycol1.find();
print(firstcoll)
coll_list=[]
for i in firstcoll:
    print(i)
    coll_list.append(i)

# edgcgf
print(type(coll_list))

dict1 = []
for i in list(coll_list):
    del i['_id']
    print(i)
    dict1.append(i)



a=json.dumps(dict1)
print(a)


from flask import Flask
app = Flask(__name__)

@app.route('/')
def collec():
        return a


if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=7070)
