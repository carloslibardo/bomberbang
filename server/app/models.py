from app import login, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128), index=True, unique=False)
	email = db.Column(db.String(128), index=True, unique=True)
	first_name = db.Column(db.String(64), index=True, unique=False)
	last_name = db.Column(db.String(64), index=True, unique=False)
	#TODO add other user information data

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
