from app import db

class character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clss = db.Column(db.String(10), nullable=False)
    race = db.Column(db.String(10), nullable=False)
    stat = db.Column(db.String(10), nullable=False)