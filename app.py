
from datetime import datetime

from flask import Flask, render_template, redirect, url_for, request

from database import Mongo
from newsletter import add_contact
from reservation import add_reservation
import mailgun
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        add_reservation(name, email, date)
    if Mongo.get('reservation', {'date':date}).count()<10:
        send(email, date)
        return render_template('booksuccess.html')
    else:
        return render_template('bookfall.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        add_contact(email)
    return redirect (url_for("home"))


def send(email, date):
    date=datetime.strptime(date,'%Y-%m-%d %H:%M')
    return requests.post(
        mailgun.URL,
        auth=("api", mailgun.API_KEY),
        data={
            "from": mailgun.FROM,
            "to": email,
            "subject": "Dog's cafe is waiting for you!",
            "text": "We will waiting for your visit! We made a reservation of a table for you on {}".format(date.strftime('%d %B %Y at %H:%M'))
        }
    )

if __name__ == '__main__':
    Mongo.connect()
    app.run(port=5001, debug=True)