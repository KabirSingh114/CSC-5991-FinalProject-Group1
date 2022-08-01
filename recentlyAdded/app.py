from flask import Flask, request, render_template, session, abort, flash
import json
import os
import pymongo
from bson.json_util import dumps, loads

app = Flask(__name__)

#can add user input to set the recentlyadded date
@app.route("/recentlyAdded", methods=['GET'])
def recently_added_list():
    mongo_client = pymongo.MongoClient('mongodb://db:27017/')
    mongo_db = mongo_client['w_books']
    mongo_coll = mongo_db['books']
    ret = dict()
    cursor = mongo_coll.find({"DateAdded" : { "$gt": "2030-07-25" } }) 
    for document in cursor:
        print(document)
        ret = document
    return dumps(ret)


if __name__ == '__main__':
    #app.secret_key = os.urandom(12)   #needed?
    app.run(host='0.0.0.0', port=5001)
