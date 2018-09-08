from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

app = Flask(__name__) #create app
app.config.from_object(Config) #load configuration from Config class(object) from ../config.py
#mongo = PyMongo(app) #not utilized
login = LoginManager(app) #LoginManager from flask to handle with logins
db = MongoEngine(app) #monogo database management with mongoengine
app.session_interface = MongoEngineSessionInterface(db) #session interface from mongoEngine

from app import routes, models
