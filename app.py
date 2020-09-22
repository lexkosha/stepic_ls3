import os.path

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/goals/<goal>/')
def goals():#Цели
    return render_template('goal.html')


@app.route('/request/')
def request_form():#
    return render_template('request.html')


@app.route('/request_done/')
def request_done_form():#
    return render_template('request_done.html')


@app.route('/booking/<id>/<day>/<id>/')
def teacher():
    return render_template('booking.html')


@app.route('/booking_done/')
def booking_done():
    return render_template('booking_done.html')


if __name__ == '__main__':
    app.run(debug=True)
    
