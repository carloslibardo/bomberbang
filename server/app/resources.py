from flask_restplus import Resource, reqparse
from flask import jsonify
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.parsers import login_parser, register_parser

class UserLogin(Resource):
    def post(self):
            data = login_parser.parse_args()
            user = User.objects(username=data['username']).first()
            if user is None or not user.check_password(data['password']):
                return {'message': 'Username or password are incorrect'}
            elif not user.check_unique_id(data['unique_id']):
                #phone who is sending request is not registered
                return {'message': 'This telephone is not registered'}
            try:
                login_user(user)
                return {'message': 'Login was succesful'}
            except:
                return {'message': 'Unknown error'}

class UserRegister(Resource):
    def post(self):
        errors = 0
        data = register_parser.parse_args()

        #This is the worst idea to deal with already in use data
        if User.objects(username=data['username']):
            errors += 1
        if User.objects(email=data['email']):
            errors += 2
        if User.objects(phone_number=data['phone_number']):
            errors += 4

        if(errors == 0):
            new_user = User(username=data['username'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'], phone_number=data['phone_number'])
            new_user.hash_password(data['password'])
            new_user.hash_unique_id(data['unique_id'])
            try:
                new_user.save()
                login_user(new_user)
                return {
                    'message': 'User registered'
                }
            except:
                return {'message': 'Unknown error'}
        elif(errors == 1):
            return {'message': 'Username is already in use'}
        elif(errors == 2):
            return {'message': 'Email is already in use'}
        elif(errors == 3):
            return {'message': 'Username and email are already in use'}
        elif(errors == 4):
            return {'message': 'Phone number is already in use'}
        elif(errors == 5):
            return {'message': 'Phone number and username are already in use'}
        elif(errors == 6):
            return {'message': 'Phone number and email are already in use'}
        elif(errors == 7):
            return {'message': 'Phone number, email and username are already in use'}

class UserLogout(Resource):
    @login_required
    def post(self):
        try:
            print(current_user.username)
            logout_user()
            return {
                'message': 'Suscessuful logout'
            }
        except:
            return {
                'message': 'Unknown error'
            }
