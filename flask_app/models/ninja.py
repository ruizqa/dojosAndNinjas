from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls): #not a useful method for this assignment, but leaving it here just in case
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    @classmethod
    def get_ninja_info(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        user = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return user
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojo)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
    @classmethod
    def update(cls, data ):
        query = "UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s, email = %(email)s , updated_at = NOW() WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )
    @classmethod
    def remove(cls, data ):
        # query = "SET SQL_SAFE_UPDATES = 0;"
        query = "DELETE FROM users WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )