from app import login, db
from os import urandom
from bcrypt import hashpw, gensalt
from werkzeug.security import safe_str_cmp
from mongoengine import *
from flask_login import UserMixin

#TODO add encryption(AES, probably)

@login.user_loader
def load_user(id):
    return User.objects(id=id).first()

#User model implementation
class User(UserMixin, db.DynamicDocument):
    username = StringField(max_length=64, require=True, unique=True)
    password_hash = StringField(max_length=512, require=True)
    email = StringField(max_length=128, require=True, unique=True)
    first_name = StringField(max_length=64, require=True)
    last_name = StringField(max_length=64, require=True)
    unique_id = StringField(max_length=64, require=True)
    phone_number = StringField(max_length=64, require=True, unique=True)

    def hash_password(self, password):
        self.password_hash = hashpw(password.encode('utf-8'), gensalt(13)).decode('utf-8')

    def check_password(self, password):
        return safe_str_cmp(hashpw(password.encode('utf-8'), self.password_hash.encode('utf-8')).decode('utf-8'), self.password_hash)

    def hash_unique_id(self, unique_id):
        self.unique_id = hashpw(unique_id.encode('utf-8'), gensalt(13)).decode('utf-8')

    def check_unique_id(self, unique_id):
        return safe_str_cmp(hashpw(unique_id.encode('utf-8'), self.unique_id.encode('utf-8')).decode('utf-8'), self.unique_id)
