from flask import Flask, request, render_template, session, abort, flash
import os
import pymongo
import json

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['w_books']
mongo_coll = mongo_db['users']

app = Flask(__name__)
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Welcome!"

@app.route('/login', methods=['POST'])
def authenticate():
    if request.form['password'] == 'password' and request.form['username'] == 'username':
        session['logged_in'] = True
    else:
        flash('Invalid Login Attempt')
    return home()

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000)
