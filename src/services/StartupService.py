import traceback
# Database
from src.database.db_mysql import get_connection
# Logger
from src.utils.Logger import Logger
# Models
from src.models.StartupModel import Startup


class StartupService():

    @classmethod
    def get_startups(cls):
        try:
            connection = get_connection()
            startups = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM startups")
                resultset = cursor.fetchall()
                for row in resultset:
                    startup = Startup(int(row[0]), row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    startups.append(startup.to_json())
            connection.close()
            return startups
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
    
     # Method for insert new startup
    @classmethod
    def saveStartup(cls, startup):
        try:
            connection = get_connection()                   
            with connection.cursor() as cursor:
                query = """INSERT INTO startups (startup_id, name, location, age, industry,founder_first_name,founder_last_name,gender,formation,user_id) 
                VALUES (NULL, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')""".format(startup.name, startup.location,startup.age,startup.industry,startup.founder_first_name,startup.founder_last_name,startup.gender,startup.formation,startup.user_id)
                print(query)
                cursor.execute(query)
                connection.commit()                                    
            connection.close()
            return "Startup add sucess"
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
    
    # Method for update startup
    @classmethod
    def updateStartup(cls, startup_id, startup):
        try:       
            connection = get_connection()            
            with connection.cursor() as cursor:
                query = """UPDATE startups SET name = '{0}',location= '{1}', age= '{2}', industry= '{3}',founder_first_name= '{4}',founder_last_name= '{5}',gender= '{6}',formation= '{7}',user_id= '{8}'
                            WHERE startup_id= '{9}'""".format(startup.name, startup.location,startup.age,startup.industry,startup.founder_first_name,startup.founder_last_name,startup.gender,startup.formation,startup.user_id, startup_id)
                print(query)
                cursor.execute(query)
                connection.commit()                                    
            connection.close()
            return "Startup updated success"
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
