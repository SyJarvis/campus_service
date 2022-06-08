# coding: utf-8
from application import db



class Class(db.Model):
    __tablename__ = 'class'

    id = db.Column(db.Integer, primary_key=True, info='id')
    name = db.Column(db.String(10, 'utf8_general_ci'), info='班级名称')
    major = db.Column(db.Integer, info='专业')
    headmaster = db.Column(db.String(8, 'utf8_general_ci'), info='班主任')
    instructor = db.Column(db.String(8, 'utf8_general_ci'), info='辅导员')
    monitor = db.Column(db.String(10, 'utf8_general_ci'), info='班长')


