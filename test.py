from asyncio.windows_events import NULL
from datetime import datetime
from flask import Flask
import json
import os
import pymongo
from faker import Faker

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['w_books']
mongo_coll = mongo_db['books']

# # mongo_db.create_collection('page1')



# cursor = mongo_db.books.find({})
# for document in cursor:
#     print(document)

# # mongo_coll.insert_one({"updated2": datetime_now})

# # cursor = mongo_db.books.find( {"DateAdded": { "$gt": "2020-07-25" } } )

cursor = mongo_coll.find({"ISBN" : "323449414257768"})
for x in cursor:
    print(x)





# # cursor = mongo_coll.find({})
# # for document in cursor:
# #     print(document)
# # mongo_db.books.find( { date: { $gt: "2020-07-25", $lte: "2020-07-31" } } )

# fake = Faker()

# book_dict = {}
# out_file = open("test.json", "w+")
# for x in range(10):
#     book_dict = ({"DateAdded": str(fake.date_between(start_date='today', end_date='+10y'))})
# json.dump(book_dict, out_file, indent = 4)
# out_file.close()


# with open('test.json') as file:
#     file_data = json.load(file)

# if isinstance(file_data, list):
#     mongo_coll.insert_many(file_data)

