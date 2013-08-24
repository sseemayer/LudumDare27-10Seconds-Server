from server import db
import datetime

class Replay(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(255))
    color = db.Column(db.String(7))
    challenge = db.Column(db.String(80))

    replay = db.Column(db.Text())

    created = db.Column(db.DateTime(), default=datetime.datetime.now)

    def __init__(self, player, color, challenge, replay):
        self.player = player
        self.color = color
        self.challenge = challenge
        self.replay = replay

    def __repr__(self):
        return '<Replay {0}: {1} on {2} (created {3})>'.format(self.id, self.player, self.challenge, self.created)


class Highscore(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(255))
    color = db.Column(db.String(7))

    score = db.Column(db.Integer)

    challenge_scores = db.Column(db.Text)

    created = db.Column(db.DateTime(), default=datetime.datetime.now)

    def __init__(self, player, color, score, challenge_scores):
        self.player = player
        self.color = color
        self.score = score
        self.challenge_scores = challenge_scores


    def __repr__(self):
        return '<Highscore {0}: {1} scored {2} (created {3})>'.format(self.id, self.player, self.score, self.created)
