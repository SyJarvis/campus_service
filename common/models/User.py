# coding: utf-8
from application import db



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, info='id')
    stu_num = db.Column(db.String(12), info='??')
    name = db.Column(db.String(20), info='??')
    member_id = db.Column(db.Integer, unique=True, info='member_id')
    class_id = db.Column(db.Integer, unique=True, info='??id')
    phone = db.Column(db.String(11), info='????')
    email = db.Column(db.String(20), info='??')
    status = db.Column(db.Integer, info='1?? 0??')
    is_admin = db.Column(db.Integer, server_default=db.FetchedValue(), info='1??? 0????')
    created_time = db.Column(db.DateTime, info='????')
    updated_time = db.Column(db.DateTime, info='????')
