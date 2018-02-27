from database import Mongo


def add_contact(email):
    Mongo.insert('dognews', {'email': email})


def get_contact():
    return Mongo.get_all('dognews')