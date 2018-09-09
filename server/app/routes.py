from app import app, db, login
from flask import jsonify, request
from flask_login import current_user, logout_user, login_user, login_required
from app.models import User

#route to login from requests
@app.route('/app/login', methods=['POST'])
def logger():
	if not request.json:
		#handle error
		json_return = [ { 'logged': False, 'cause': 'miss request arguments' } ]
		return jsonify({'resp': json_return})
	elif current_user.is_authenticated:
		#handle
		json_return = [ { 'logged': True, 'cause': 'user is already logged' } ]
		return jsonify({'resp': json_return})
	else:
		usr = request.json['username']
		print(usr)
		password = request.json['password']
		print(password)
		user = User.objects(username=usr).first()
		if user is None or not user.check_password(password):
			#handle login error(username or password are incorrect)
			json_return = [ { 'logged': False, 'cause': 'password or user incorrect' } ]
			return jsonify({'resp': json_return})
		login_user(user, remember=True)
		json_return = [ { 'logged': True, 'cause': 'user data are correct' } ]
		return jsonify({'resp': json_return})
	json_return = [ { 'logged': 'Unknown', 'cause': 'not handled request' } ]
	return jsonify({'resp': json_return})

