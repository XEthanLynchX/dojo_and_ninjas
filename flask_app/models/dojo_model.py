from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja_model

db = 'dojos_and_ninjas'

class Dojo:
    
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.location = db_data['location']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas= []
        # self.ninjas is used to append ninjas objects from the ninja_model import at the top
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        #the '   ' is the database
        print(results)
        # Create an empty list to append our instances of dojo
        # s
        dojos= []
        # Iterate over the db results and create instances of dojo
        # s with cls.
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def save_dojo(cls, form_data):
        query= 'INSERT INTO dojos(name,location) VALUES( %(name)s, %(location)s);'
        return connectToMySQL(db).query_db(query, form_data)

    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'dojos_id' : row['dojos_id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( ninja_model.Ninja(n) )
        return dojo
