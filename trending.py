from flask import Flask

import json
import os


app = Flask(__name__)

with open("../URL HERE") as f: #replace with db get 
    trending = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    return json.dumps({
        "uri": "/",
        "subresource_uris": {
            "trending": "/trending",
        }
    })


@app.route("/trending", methods=['GET'])
def trending_list():
    return json.dumps(trending)


if __name__ == '__main__':
    #app.secret_key = os.urandom(12) #needed?
    app.run(host='0.0.0.0', port=5000)
