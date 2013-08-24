import os
from flask import Flask
from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Nothing to see here, move along!'

@app.route('/highscores')
def highscores_list():

    out = []
    for highscore in db.session.query(models.Highscore).order_by(models.Highscore.score.desc()):
        out.append({
            'player': highscore.player,
            'color': highscore.color,
            'score': highscore.score
        })


    return out
