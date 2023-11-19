import traceback
# Database
from src.database.db_mysql import get_connection
# Logger
from src.utils.Logger import Logger
# Models
from src.models.UserModel import User


class UserService():

    @classmethod
    def get_users(cls):
        try:
            connection = get_connection()
            users = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                resultset = cursor.fetchall()
                for row in resultset:
                    user = User(int(row[0]), row[1],row[2],row[3],row[4],row[5],bool(row[6]))
                    users.append(user.to_json())
            connection.close()
            return users
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())


     # Method for update user
    @classmethod
    def updateUser(cls, user_id, user):
        try:       
            connection = get_connection()            
            with connection.cursor() as cursor:
                query = """UPDATE users SET first_name = '{0}',last_name= '{1}', email= '{2}', username= '{3}',password= '{4}',enabled= '{5}'
                            WHERE user_id= '{6}'""".format(user.first_name, user.last_name,user.email,user.username,user.password,user.enabled,user_id)
                print(query)
                cursor.execute(query)
                connection.commit()                                    
            connection.close()
            return "User updated success"
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
