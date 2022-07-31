from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
import json
from bson.json_util import dumps
import requests
from werkzeug.utils import redirect

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['w_books']
mongo_users_coll = mongo_db['users']

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome!"


@app.route('/users', methods=['GET'])
def users_list():
    users_data = mongo_users_coll.find()
    return dumps(users_data)


@app.route('/users/<username>', methods=['GET'])
def user_by_username(username):
    user_data = mongo_users_coll.find_one({"Username": username})
    hide_password = {"Password": ""}
    user_data.update(hide_password)
    return dumps(user_data)

@app.route('/users/<email>', methods=['GET'])
def user_by_email(email):
    user_data = mongo_users_coll.find_one({"Email": email})
    hide_password = {"Password": ""}
    user_data.update(hide_password)
    return dumps(user_data)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5002)
