from datetime import datetime
from . import db

class Tracker(db.Model):
    __tablename__ = 'trackers'

    id = db.Column(db.Integer,primary_key = True)
    tracker_name = db.Column(db.String(255))
    comment=db.Column(db.String())
    rate=db.Column(db.Integer)
    updated = db.Column(db.DateTime,default=datetime.utcnow)

    def save_tracker(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Tracker {self.tracker_name}'

class Logs(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    comment=db.Column(db.String())
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    rate=db.Column(db.Integer)
    tracker_id = db.Column(db.Integer,db.ForeignKey("trackers.id"))

    def save_log(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'Tracker {self.name}'