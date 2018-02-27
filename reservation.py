from database import Mongo


def add_reservation(name, email, date):
    Mongo.insert('reservation',{'name': name, 'email': email, 'date': date})


def get_reservation():
    return Mongo.get_all('reservation')
