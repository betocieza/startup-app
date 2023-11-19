from flask import Blueprint, request, jsonify
from src.models.FactorModel import Factor

# Security
from src.utils.Security import Security
# Services
from src.services.FactorService import FactorService

main = Blueprint('factor_blueprint', __name__)

@main.route('/all', methods=['GET'])
def get_factors(): 
    has_access = Security.verify_token(request.headers)
    print(has_access)
    if has_access:
        try:
            factors = FactorService.get_factors()
            if (len(factors) > 0):
                return jsonify(factors)
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
    

@main.route('/<factor_id>', methods=['GET'])
def get_factor_by_id(factor_id):
     has_access = Security.verify_token(request.headers) 
     print(has_access) 
     if has_access:
        try:
            factor = FactorService.getFactorById(factor_id)          
            if factor!= None:
                return jsonify(factor)
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
     else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
     
@main.route('/add', methods=['POST'])
def add_factor():
     has_access = Security.verify_token(request.headers) 
     print(has_access) 
     if has_access:
        try:
            
            name = request.json['name']
            description = request.json['description']

            _factor = Factor(0,name, description)            

            if FactorService.saveFactor(_factor):
                return jsonify("success")
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
     else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
     
@main.route('/update/<factor_id>', methods=['PUT'])
def update_factor(factor_id):
    has_access = Security.verify_token(request.headers) 
    print(has_access) 
    if has_access:
        try:            
            name = request.json['name']
            description = request.json['description']
            factor = Factor(0, name, description)            

            if FactorService.updateFactor(factor_id, factor):
                return jsonify(" success")
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401