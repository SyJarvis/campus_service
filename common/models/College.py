# coding: utf-8
from application import db



class College(db.Model):
    __tablename__ = 'college'

    id = db.Column(db.Integer, primary_key=True, info='id')
    name = db.Column(db.String(20, 'utf8_general_ci'), info='学院名称')
    campus_position = db.Column(db.String(8, 'utf8_general_ci'), nullable=False, info='校区名称')
