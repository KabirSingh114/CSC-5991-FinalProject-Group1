from flask import Flask

import json
import os

app = Flask(__name__)

with open("../URL HERE") as f:
    recently_added = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    return json.dumps({
        "uri": "/",
        "subresource_uris": {
            "recently_added": "/recentlyAdded",
        }
    })


@app.route("/recentlyAdded", methods=['GET'])
def recently_added_list():
    return json.dumps(recently_added)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)   #needed? or just last line
    app.run(host='0.0.0.0', port=5000)
