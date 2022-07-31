from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
import json
from bson.json_util import dumps
import requests
from werkzeug.utils import redirect

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['w_books']
mongo_books_coll = mongo_db['books']

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome!"


@app.route('/books', methods=['GET'])
def books_list():
    books_data = mongo_books_coll.find()
    return dumps(books_data)


@app.route('/books/<ISBN>', methods=['GET'])
def book_info(isbn):
    book_data = mongo_books_coll.find_one({"ISBN": isbn})
    return dumps(book_data)


@app.route('/books/<genre>', methods=['GET'])
def genre_info(genre):
    genre_data = mongo_books_coll.find({"Genre": genre})
    return dumps(genre_data)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5004)
