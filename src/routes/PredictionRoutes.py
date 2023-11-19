from flask import Blueprint, request, jsonify

from src.models.PredictionModel import Prediction
import json
import datetime
import numpy as np
import pickle
import os
# Security
from src.utils.Security import Security
# Services
from src.services.PredictionService import PredictionService
from src.services.MLProcessService import MLProcessService
# Logger
from src.utils.Logger import Logger
import traceback
main = Blueprint('prediction_blueprint', __name__)


@main.route('/all', methods=['GET'])
def get_predictions(): 
    has_access = Security.verify_token(request.headers)
    print(has_access)
    if has_access:
        try:
            predictions = PredictionService.get_predictions()
            if (len(predictions) > 0):
                return jsonify(predictions)
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
    
@main.route('/pre', methods=['GET'])
def get_predictions_res(): 
    has_access = Security.verify_token(request.headers)
    print(has_access)
    if has_access:
        try:
            predictions = PredictionService.getPredictionStartup()
         
            if (len(predictions) > 0):
                return jsonify(predictions)
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
    


@main.route('/create', methods=['POST'])
def add_prediction():
     has_access = Security.verify_token(request.headers) 
     
     if has_access:
        try:                       
            location = request.json['location']            
            age_startup = request.json['age_startup']
            size_startup = request.json['size_startup'] 
            count_profile_skill = request.json['count_profile_skill']
            company_total_revenue = request.json['company_total_revenue']
            export_cti_products = request.json['export_cti_products']
            main_innovation_activities = request.json['main_innovation_activities']
            investment_rd= request.json['investment_rd']
            domestic_economic_enviroment= request.json['domestic_economic_enviroment']
            availability_skill_employees= request.json['availability_skill_employees']
            access_finance= request.json['access_finance']
            cost_rd= request.json['cost_rd']
            availability_infraestructure= request.json['availability_infraestructure']
            innovative_enviroment= request.json['innovative_enviroment']
            goverment_regulation= request.json['goverment_regulation']
            access_target_market= request.json['access_target_market']
            global_economic_enviroment= request.json['global_economic_enviroment']
            exchange_rates= request.json['exchange_rates']
            competitive_enviroment= request.json['competitive_enviroment']
            access_export_market= request.json['access_export_market']

            factors = np.array( [location, age_startup,size_startup,count_profile_skill, company_total_revenue,export_cti_products,main_innovation_activities,investment_rd,domestic_economic_enviroment,availability_skill_employees,access_finance,cost_rd,availability_infraestructure,	innovative_enviroment,goverment_regulation,access_target_market,global_economic_enviroment,exchange_rates,competitive_enviroment,access_export_market])            
            prediction_result = MLProcessService.predictionModel(factors)           
            created_at=datetime.datetime.utcnow()        
            startup_id = request.json['startup_id']
            
            _prediction = Prediction(0,location, age_startup,size_startup,count_profile_skill, company_total_revenue,export_cti_products,main_innovation_activities,investment_rd,domestic_economic_enviroment,availability_skill_employees,access_finance,cost_rd,availability_infraestructure,	innovative_enviroment,goverment_regulation,access_target_market,global_economic_enviroment,exchange_rates,competitive_enviroment,access_export_market,prediction_result,created_at, startup_id)            

            if PredictionService.savePrediction(_prediction):
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
     
