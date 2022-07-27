from datetime import date
from flask import Flask

import json
import os
import pymongo
from datetime import date
from faker import Faker
# mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
# mongo_db = mongo_client['w_books']

# print(mongo_db.recently_added.find())


fake = Faker()
print(fake.date_between(start_date='today', end_date='+10y'))