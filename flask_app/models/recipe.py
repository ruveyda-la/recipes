from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL 
from flask_app.models.user import User
from flask_app import flash




class Recipe:
    db="recipes"

    def __init__(self,data):
        self.id = data['id']     
        self.name = data['name'] 
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30 = data['under_30'] 
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posted_by=None

    @classmethod
    def save (cls, data):
        query = """INSERT INTO recipes (name,description,instruction,under_30,date_made,user_id)
                VALUES (%(name)s,%(description)s,%(instruction)s,%(under_30)s,%(date_made)s,%(user_id)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_all_recipes(cls):
        query = """SELECT * FROM recipes
                    LEFT JOIN users ON users.id=recipes.user_id;"""
        
        results = connectToMySQL(cls.db).query_db(query)
    # this will give us list of dictionaries let's convert to instances of the Recipe class
        recipes = []
        
        for result in results:
            recipe = cls(result)
            recipes.append( recipe )
            user_info = {
                'id' : result['users.id'],
                'first_name':result['first_name'],
                'last_name':result['last_name'],
                'email':result['email'],
                'password':result['password'],
                'created_at':result['users.created_at'],
                'updated_at':result['users.updated_at']
                }
            recipe.posted_by=User(user_info)
            
        return recipes

    @staticmethod
    def validate_recipe(recipe):
    
        is_valid = True
        if len(recipe['name'])<3:
            flash("Name must be at least 3 characters!")
            is_valid = False
        if len(recipe['description'])<3:
            flash("Description  must be at least 3 characters!")
            is_valid = False
        if len(recipe['instruction'])<3:
            flash("Instruction  must be at least 3 characters!")
            is_valid = False
        if 'under_30' not in recipe:
            flash("All fields required!")
            is_valid = False
        if len(recipe['date_made']) == 0:
            flash("All fields required!")
            is_valid = False


        return is_valid
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id=recipes.user_id WHERE recipes.id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,{'id':id})
        recipe = result[0]
        return recipe 

    @classmethod
    def change(cls,data):
        query="""UPDATE recipes SET name=%(name)s, description=%(description)s,
                instruction=%(instruction)s,date_made=%(date_made)s,under_30=%(under_30)s,user_id=%(user_id)s
                WHERE id=%(id)s;"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM recipes  WHERE recipes.id= %(id)s;"
        result=connectToMySQL(cls.db).query_db(query,{'id':id})
        return result 




