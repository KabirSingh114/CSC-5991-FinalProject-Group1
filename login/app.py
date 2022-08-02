from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
import json
import requests
from bson.json_util import dumps

mongo_client = pymongo.MongoClient('mongodb://db:27017/')
mongo_db = mongo_client['w_books']
mongo_coll = mongo_db['users']
mongo_users_coll = mongo_db['users']

app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        user_profile = requests.get("http://users:5000/users/{}".format(session.get('user')))
        user_profile = user_profile.json()

        return render_template('index.html', user_profile=user_profile)


@app.route('/login', methods=['POST'])
def authenticate():
    print(request)
    query = {"Username": request.form['username'], "Password": request.form['password']}
    valid_login = mongo_users_coll.count_documents(query)
    if valid_login > 0:
        session['logged_in'] = True
        session['user'] = request.form['username']
    else:
        flash('Invalid Login Attempt')
    return home()


@app.route('/search', methods=['POST'])
def book_search():
    print(request.form['search'])
    print(request.form['option'])

    build_call_url = "http://books:5000/books/" + request.form['option'] + "/{}"
    print(build_call_url)

    search_result = requests.get(build_call_url.format(request.form['search']))
    search_result = search_result.json()

    return render_template('results.html', search_result=search_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')