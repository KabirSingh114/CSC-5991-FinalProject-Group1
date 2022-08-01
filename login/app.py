from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
import json
import requests
from werkzeug.utils import redirect

mongo_client = pymongo.MongoClient('mongodb://db:27017/')
mongo_db = mongo_client['w_books']
mongo_coll = mongo_db['users']
mongo_users_coll = mongo_db['users']

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    if session.get('logged_in'):
        user_profile = requests.get("http://users:5000/users/{}".format(session.get('user')))  #some problem with getting this api call
        user_profile = user_profile.json()
        welcome_message = "Welcome " + user_profile["First_Name"] + "!"
        return welcome_message
    return render_template('login.html')

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


if __name__ == '__main__':
    app.run(host='0.0.0.0')