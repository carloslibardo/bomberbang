from app import login, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from mongoengine import *

#creates a method to load a user in login from its id
@login.user_loader
def load_user(search_id):
	return User.objects(id=search_id).first()

#creates a User model to save user data
class User(UserMixin, db.DynamicDocument):
	username = StringField(max_length=64, require=True, unique=True)
	password_hash = StringField(max_length=128, require=True)
	email = StringField(max_length=128, require=True, unique=True)
	first_name = StringField(max_length=64, require=True)
	last_name = StringField(max_length=64, require=True)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

