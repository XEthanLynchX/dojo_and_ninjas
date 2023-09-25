from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_and_ninjas'

class Ninja:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.dojos_id = db_data['dojos_id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

#crud commands for the database

    @classmethod
    def save_ninja(cls, form_data):
        query= 'INSERT INTO ninjas(first_name, last_name, age, dojos_id) VALUES( %(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s );'
        return connectToMySQL(db).query_db(query, form_data)