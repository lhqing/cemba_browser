from flask import Flask, render_template, jsonify
import requests
from random import randint
from flask_cors import CORS
from db.query_compute_db import *


app = Flask(__name__,
            static_folder="../dist/static",
            template_folder="../dist")
if app.debug:
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    # cors is for allowing other origin (e.g. the node.js server from frontend dev)
    # to access apis in backend. If close, only flask server can use api


@app.route('/api/random')  # toy api for test
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/api/tsne')  # toy api for test
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)





@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # because we use vue-router html5 history mode,
    # we will point any backend routes into index.html,
    # and let vue-router to handle

    if app.debug:
        # if app is in debug mode, let flask proxy front-end server
        text = requests.get('http://localhost:8080/{}'.format(path)).text
        # this makes flask server been able to proxy front-end server,
        # therefore we cau use frontend updates without run npm build
        return text
    return render_template("index.html")





