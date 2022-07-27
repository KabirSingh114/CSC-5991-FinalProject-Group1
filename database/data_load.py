import pymongo
import json

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['w_books']
mongo_db.create_collection('books')
mongo_coll = mongo_db['books']

print(mongo_db.list_collection_names())

with open('book_list.json') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    mongo_coll.insert_many(file_data)
else:
    mongo_coll.insert_one(file_data)

cursor = mongo_coll.find({})
for document in cursor:
    print(document)


