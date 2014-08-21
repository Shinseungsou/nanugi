"""
models.py

"""
from apps import db


class member_info(db.Model):
    email = db.Column(db.String(255))
    member_id = db.Column(db.Integer, primary_key=True)
    facebook_id = db.Column(db.Integer) #temp

class moim(db.Model):
    moim_id = db.Column(db.Integer, primary_key=True)
    moim_name = db.Column(db.String(255))
    member_id = db.Column(db.Integer, primary_key=True)

class moim_join(db.Model):
    moim_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(255))
    invited = db.Column(db.Integer)

class moim_pay(db.Model):
    moim_id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    payment_all = db.Column(db.Integer)
    moim_date = db.Column(db.DateTime(), default=db.func.now())
