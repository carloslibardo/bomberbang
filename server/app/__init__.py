from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_restplus import Api
from flask_login import LoginManager

app = Flask(__name__) #create flask app
app.config.from_object(Config) #load app configuration from Config object
login = LoginManager(app)
api = Api(app) #api for resources in app
db = MongoEngine(app) #db management
app.session_interface = MongoEngineSessionInterface(db) #database login session

from app import models, routes
from app.resources import UserLogin, UserRegister, UserLogout

#adding resources list into the app api, with its route and class
api.add_resource(UserLogin, '/app/login')
api.add_resource(UserRegister, '/app/register')
api.add_resource(UserLogout, '/app/logout')
