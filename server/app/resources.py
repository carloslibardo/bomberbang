from flask_restplus import Resource, reqparse
from flask import jsonify
from app.models import User, RevokedToken
from app.parsers import login_parser, register_parser
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from flask_login import current_user, login_user, logout_user, login_required

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
                access_token = create_access_token(identity=data['username'])
                refresh_token = create_refresh_token(identity=data['username'])
                return {
                    'message': 'Login was succesful',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
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
                access_token = create_access_token(identity=data['username'])
                refresh_token = create_refresh_token(identity=data['username'])
                return {
                    'message': 'User registered',
                    'access_token': access_token,
                    'refresh_token': refresh_token
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

#refresh the access token providing refresh token
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {
            'access_token': access_token
        }

#revoke user access token, loggout partially
class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.save()
            return{'message': 'Revoked access token'}
        except:
            return{'message': 'Error in revoking access token'}

#revoke user refresh token, loggout permanent
class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.save()
            return{'message': 'Revoked refresh token'}
        except:
            return{'message': 'Error in revoking refresh token'}

#loggout a user by session and token
class UserLogout(Resource):
    @login_required
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        if jti is not None:
            try:
                revoked_toke = RevokedToken(jti=jti)
                revoked_token.save()
                logout_user()
                return{'message': 'User was log out and access token was revoked'}
            except:
                return{'message': 'Erro when logging out user'}
        else:
            try:
                logout_user()
                return{'message': 'User was log out'}
            except:
                return{'message': 'Error when logging out user'}
