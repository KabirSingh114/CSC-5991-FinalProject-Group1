from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
from datetime import datetime
import json
from bson.json_util import dumps, loads

app = Flask(__name__)


@app.route('/topten', methods=['GET'])
def rental():
    mongo_client = pymongo.MongoClient('mongodb://db:27017/')
    mongoDb = mongo_client['w_books']
    bookCollection = mongoDb['books']
    data = bookCollection.find().sort('rental_count',-1).limit(10)

    return dumps(data)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5008)
