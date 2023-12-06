from flask import Blueprint, request, jsonify, session
from src.models.StartupModel import Startup
# Logger
from src.utils.Logger import Logger
import traceback
# Security
from src.utils.Security import Security
# Services
from src.services.StartupService import StartupService

main = Blueprint('startup_blueprint', __name__)


@main.route('/all', methods=['GET'])
def get_startups(): 
    has_access = Security.verify_token(request.headers)
    print(has_access)
    if has_access:
        try:
            startups = StartupService.get_startups()
            if (len(startups) > 0):
                return jsonify(startups)
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
    
@main.route('/create', methods=['POST'])
def add_startup():
    has_access = Security.verify_token(request.headers) 
    print(has_access) 
    if has_access:
        try:           
            name = request.json['name']
            location = request.json['location']          
            age= request.json['age']  
            industry= request.json['industry'] 
            founder_first_name= request.json['founder_first_name'] 
            founder_last_name= request.json['founder_last_name'] 
            gender= request.json['gender'] 
            formation= request.json['formation'] 
            #user_id= request.json['user_id'] 
            user_id= 1 
            _startup = Startup(0,name,location,age,industry,founder_first_name,founder_last_name, gender,formation,user_id)            
           
            if StartupService.saveStartup(_startup):
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

@main.route('/update/<startup_id>', methods=['PUT'])
def update_startup(startup_id):
    has_access = Security.verify_token(request.headers) 
    print(has_access) 
    if has_access:
        try:            
            name = request.json['name']
            location = request.json['location']          
            age= request.json['age']  
            industry= request.json['industry'] 
            founder_first_name= request.json['founder_first_name'] 
            founder_last_name= request.json['founder_last_name'] 
            gender= request.json['gender'] 
            formation= request.json['formation']            
            user_id= 2

            startup = Startup(0, name, location, age, industry,founder_first_name,founder_last_name,gender,formation,user_id)            

            if StartupService.updateStartup(startup_id, startup):
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
