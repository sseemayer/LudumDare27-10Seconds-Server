import os
from flask import Flask
from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Nothing to see here, move along!'

@app.route('/highscores')
def highscores_list():
    return []
