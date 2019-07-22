from flask import Flask
from flask_bootstrap import Bootstrap
from pymongo import MongoClient

app = Flask(__name__)
Bootstrap(app)

try:
    __client = MongoClient(host='127.0.0.1', port=27017)
    db = __client['emr']
except Exception as e:
    print(e)

import application.views