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
    member_id = db.Column(db.Integer, db.ForeignKey('member_info.member_id'), primary_key=True, autoincrement=False)
    member_info = db.relationship('member_info', backref=db.backref('moim', cascade='all, delete-orphan', lazy='dynamic'))
    #member_id = member_info.member_id

class moim_join(db.Model):
    moim_id = db.Column(db.Integer, db.ForeignKey('moim.moim_id'), primary_key=True, autoincrement=False)
    moim = db.relationship('moim', backref=db.backref('moim_join', cascade='all, delete-orphan', lazy='dynamic'))
    # moim_id = moim.moim_id
    member_id = db.Column(db.Integer, db.ForeignKey('member_info.member_id'), primary_key=True, autoincrement=False)
    member_info = db.relationship('member_info', backref=db.backref('moim_join', cascade='all, delete-orphan', lazy='dynamic'))
    #member_id = member_info.member_id
    member_name = db.Column(db.String(255))
    invited = db.Column(db.Integer)

class moim_pay(db.Model):
    moim_id = db.Column(db.Integer, db.ForeignKey('moim.moim_id'), primary_key=True, autoincrement=False)
    moim = db.relationship('moim', backref=db.backref('moim_pay', cascade='all, delete-orphan', lazy='dynamic'))
    # moim_id = moim.moim_id
    number = db.Column(db.Integer, primary_key=True, autoincrement=False)
    content = db.Column(db.String(255))
    payment_all = db.Column(db.Integer)
    moim_date = db.Column(db.DateTime(), default=db.func.now())

class moim_mem(db.Model):
    moim_id = db.Column(db.Integer, db.ForeignKey('moim.moim_id'), primary_key=True, autoincrement=False)
    moim = db.relationship('moim', backref=db.backref('moim_mem', cascade='all, delete-orphan', lazy='dynamic'))
    member_id = db.Column(db.Integer, db.ForeignKey('member_info.member_id'), primary_key=True, autoincrement=False)
    member_info = db.relationship('member_info', backref=db.backref('moim_mem', cascade='all, delete-orphan', lazy='dynamic'))
