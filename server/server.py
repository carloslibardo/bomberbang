from app import app
from app.models import User

if __name__ == '__main__':
	#creation of admin user for first user and tests
	admin_user = None
	for user in User.objects():
		if user.username=='admin':
			admin_user = user
	if admin_user is None:
		admin_user = User(username='admin', email='admin@admin.com', first_name='App', last_name='Administrator')
		admin_user.set_password('admin')
		admin_user.save()

	#runs app to be located from any device in the local network
	app.run(host='0.0.0.0')
