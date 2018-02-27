import pymongo

class Mongo:
    client = None
    database=None


    @staticmethod
    def connect():
        Mongo.client=pymongo.MongoClient('mongodb://localhost:27017/')
        Mongo.database = Mongo.client['reservation']


    @staticmethod
    def insert (collection, data):
        Mongo.database[collection].insert(data)

    @staticmethod
    def get_all(collection):
        return Mongo.database[collection].find()

    @staticmethod
    def get(collection, query):
        return Mongo.database[collection].find(query)