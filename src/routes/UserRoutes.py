from flask import Blueprint, request, jsonify
from src.models.UserModel import User
# Logger
from src.utils.Logger import Logger
import traceback

# Security
from src.utils.Security import Security
# Services
from src.services.UserService import UserService

main = Blueprint('user_blueprint', __name__)


@main.route('/all', methods=['GET'])
def get_users(): 
    has_access = Security.verify_token(request.headers)
    print(has_access)
    if has_access:
        try:
            users = UserService.get_users()
            if (len(users) > 0):              
                return jsonify(users)
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

@main.route('/update/<user_id>', methods=['PUT'])
def update_user(user_id):
    has_access = Security.verify_token(request.headers) 
    print(has_access) 
    if has_access:
        try:            
                    
            first_name = request.json['first_name'] 
            last_name = request.json['last_name'] 
            email = request.json['email'] 
            username = request.json['username'] 
            password = request.json['password'] 
            enabled = request.json['enabled']          
          
            user = User(0, first_name, last_name,email,username,password,enabled)            

            if UserService.updateUser(user_id, user):
                return jsonify(" success")
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
