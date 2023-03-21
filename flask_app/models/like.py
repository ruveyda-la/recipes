from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL 

from flask_app import session




class Like:
    db="recipes"

    def __init__(self,data):
        self.id = data['id']     
        self.user_id = data['user_id'] 
        self.recipe_id = data['recipe_id']
        self.created_at= data['created_at']
        self.updated_at=data['updated_at']


    @classmethod
    def delete_like(cls, user_id,recipe_id):
        
        query = "DELETE FROM likes WHERE recipe_id= %(recipe_id)s AND user_id=%(user_id)s;"
        result=connectToMySQL(cls.db).query_db(query,{'user_id':user_id,'recipe_id':recipe_id})
        return result

    @classmethod
    def count_like(cls,recipe_id):
        query = "SELECT COUNT(*) FROM likes WHERE recipe_id = %(recipe_id)s;"
        result=connectToMySQL(cls.db).query_db(query,{'recipe_id':recipe_id})
        print (result)
        return result[0]['COUNT(*)'] 


    @classmethod
    def save_like(cls):
        user_id = session['user_id']
        recipe_id=session['recipe_id']
        query = "INSERT INTO likes (user_id,recipe_id) VALUES (%(user_id)s,%(recipe_id)s)"
        result=connectToMySQL(cls.db).query_db(query,{'user_id':user_id,'recipe_id':recipe_id})
        return result

    @classmethod
    def get_like(cls,user_id,recipe_id):
        
        query = "SELECT * FROM likes WHERE recipe_id= %(recipe_id)s AND user_id=%(user_id)s;"
        result=connectToMySQL(cls.db).query_db(query,{'user_id':user_id,'recipe_id':recipe_id})
        return result[0] if result else None 

        

        
