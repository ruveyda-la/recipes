from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL 




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

    @classmethod
    def save (cls, data):
        query = """INSERT INTO recipes (name,description,instruction,under_30,date_made,user_id)
                VALUES (%(name)s,%(description)s,%(instruction)s,%(under_30)s,%(date_made)s,%(user_id)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_all_recipes(cls):
        query = """SELECT * FROM users
                    LEFT JOIN recipes ON users.id=recipes.user_id;"""
        
        results = connectToMySQL(cls.db).query_db(query)
    
        users = []
    
        for result in results:
            users.append( cls(result) )
        return users

