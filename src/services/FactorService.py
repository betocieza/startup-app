import traceback
# Database
from src.database.db_mysql import get_connection
# Logger
from src.utils.Logger import Logger
# Models
from src.models.FactorModel import Factor


class FactorService():
    
    @classmethod
    def get_factors(cls):
        try:
            connection = get_connection()
            factors = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM factors")
                resultset = cursor.fetchall()
                for row in resultset:
                    factor = Factor(int(row[0]), row[1],row[2])
                    factors.append(factor.to_json())
            connection.close()
            return factors
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())



    @classmethod
    def getFactorById(cls,factor_id):
        try:
            connection = get_connection()   
           # Factor = []        
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM factors WHERE factor_id = '{0}'".format(factor_id))
                data = cursor.fetchone()              
                if data!=None:
                    factor = {'factor_id':data[0],'name':data[1],'description':data[2]} 
                    print(factor)                   
            connection.close()
            return factor
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
    
    # Method for insert new factor
    @classmethod
    def saveFactor(cls, factor):
        try:
            connection = get_connection()                   
            with connection.cursor() as cursor:
                query = """INSERT INTO factors (factor_id, name, description) 
                VALUES (NULL, '{0}', '{1}')""".format(factor.name, factor.description)
                print(query)
                cursor.execute(query)
                connection.commit()                                    
            connection.close()
            return "Factor add sucess"
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    # Method for update factor
    @classmethod
    def updateFactor(cls, factor_id, factor):
        try:       
            connection = get_connection()            
            with connection.cursor() as cursor:
                query = """UPDATE factors SET name = '{0}',description = '{1}'
                            WHERE factor_id= '{2}'""".format(factor.name, factor.description, factor_id)
                print(query)
                cursor.execute(query)
                connection.commit()                                    
            connection.close()
            return "Factor updated sucess"
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
