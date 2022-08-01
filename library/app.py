from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
from datetime import datetime
import json
from bson.json_util import dumps, loads

mongo_client = pymongo.MongoClient('mongodb://db:27017/')
mongo_db = mongo_client['w_books']
bookCollection = mongoDb['books_rentals']
app = Flask(__name__)


@app.route('/library/<renter_name>', methods=['GET'])
def get_library(renter_name):
    genre_data = bookCollection.find({"renter_name": renter_name})
    return dumps(genre_data)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5005)
