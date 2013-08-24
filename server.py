import os
import flask
from flask import request
from flask.ext.heroku import Heroku
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
heroku = Heroku(app)

if not app.config['SQLALCHEMY_DATABASE_URI']:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/ld27-replays'


db = SQLAlchemy(app)

import models

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
            'score': highscore.score,
            'created': highscore.created
        })


    return flask.jsonify(highscores=out)


@app.route('/highscores', methods=('POST',))
def highscore_add():

    player = request.form['player']
    color = request.form['color']
    score = request.form['score']
    challenge_scores = request.form['challenge_scores']

    hs = models.Highscore(player, color, score, challenge_scores)

    db.session.add(hs)
    db.session.commit()

    return "OK"


@app.route('/replays/<challenge>')
def replays_list(challenge):

    out = []
    for replay in db.session.query(models.Replay).filter(models.Replay.challenge == challenge):
        out.append({
            'player': replay.player,
            'color': replay.color,
            'replay': replay.replay,
            'created': replay.created

        })

    return flask.jsonify(replays=out, challenge=challenge)


@app.route('/replays', methods=('POST',))
def replays_post():

    player = request.form['player']
    color = request.form['color']
    challenge = request.form['challenge']
    replay = request.form['replay']

    rp = models.Replay(player, color, challenge, replay)

    db.session.add(rp)
    db.session.commit()

    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
