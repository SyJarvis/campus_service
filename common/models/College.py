# coding: utf-8
from application import db



class College(db.Model):
    __tablename__ = 'college'

    id = db.Column(db.Integer, primary_key=True, info='id')
    name = db.Column(db.String(20), info='????')
    campus_position = db.Column(db.String(20), info='??')
    school_id = db.Column(db.ForeignKey('university.id'), index=True, info='??id')
    created_time = db.Column(db.DateTime, info='????')
    updated_time = db.Column(db.DateTime, info='????')

    school = db.relationship('University', primaryjoin='College.school_id == University.id', backref='colleges')



class University(db.Model):
    __tablename__ = 'university'

    id = db.Column(db.Integer, primary_key=True, info='id')
    name = db.Column(db.String(20), info='????')
    code = db.Column(db.String(10), info='?????')
    depart = db.Column(db.String(15), info='????')
    location = db.Column(db.String(10), info='???')
    level = db.Column(db.Enum('??', '??'), info='????')
    type = db.Column(db.Enum('??', '??'), info='????')
    status = db.Column(db.Integer, info='1?? 0??')
    updated_time = db.Column(db.DateTime, info='????')
    created_time = db.Column(db.DateTime, info='????')
