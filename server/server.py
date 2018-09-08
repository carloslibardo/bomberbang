from app import app

if __name__ == '__main__':
	#runs app to be located from any device in the local network
	app.run(host='0.0.0.0')
