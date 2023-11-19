import traceback
# Database
from src.database.db_mysql import get_connection
# Logger
from src.utils.Logger import Logger



# Models
from src.models.PredictionModel import Prediction, PredictionResult


class PredictionService():

    @classmethod
    def get_predictions(cls):
        try:
            connection = get_connection()
            predictions = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM predictions")               
                resultset = cursor.fetchall()
                for row in resultset:
                    prediction = Prediction(int(row[0]), row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],
                                      int(row[10]), row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],
                                      int(row[20]), row[21],row[22],row[23] )
                    

                    predictions.append(prediction.to_json())
            connection.close()
            return predictions
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
    
    @classmethod
    def getPredictionStartup(cls):
        try:
            connection = get_connection()
            predictions = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT P.prediction_id, P.prediction_result, P.created_at, E.startup_id,E.name FROM predictions P JOIN startups E ON P.startup_id = E.startup_id ORDER BY P.created_at DESC")               
                resultset = cursor.fetchall()
                for row in resultset:
                    prediction = PredictionResult(int(row[0]), int(row[1]),row[2],row[3], row[4])              
                    predictions.append(prediction.to_json())
            connection.close()
            return predictions
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
    

    # Method for insert new prediction
    @classmethod
    def savePrediction(cls, prediction):
        try:
            connection = get_connection()                   
            with connection.cursor() as cursor:
                query = """INSERT INTO predictions VALUES (NULL, '{0}', '{1}' ,'{2}','{3}','{4}','{5}','{6}' ,'{7}','{8}','{9}','{10}', '{11}', '{12}','{13}','{14}','{15}','{16}' ,'{17}','{18}','{19}','{20}','{21}','{22}'
                )""".format(prediction.location, prediction.age_startup,prediction.size_startup,prediction.count_profile_skill, 
                            prediction.company_total_revenue,prediction.export_cti_products,prediction.main_innovation_activities,prediction.investment_rd,
                            prediction.domestic_economic_enviroment,prediction.availability_skill_employees,prediction.access_finance,prediction.cost_rd,
                            prediction.availability_infraestructure,prediction.innovative_enviroment,prediction.goverment_regulation,
                            prediction.access_target_market,prediction.global_economic_enviroment,prediction.exchange_rates,
                            prediction.competitive_enviroment,prediction.access_export_market,prediction.prediction_result,prediction.created_at,prediction.startup_id)
                print(query)
                cursor.execute(query)
                connection.commit()                                    
            connection.close()
            return "prediction add sucess"
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

   