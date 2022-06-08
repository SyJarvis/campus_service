# coding: utf-8
from application import db



class Major(db.Model):
    __tablename__ = 'major'

    id = db.Column(db.Integer, primary_key=True, info='id')
    name = db.Column(db.String(15, 'utf8_general_ci'), unique=True, info='专业名称')
    college = db.Column(db.Integer, info='学院')
