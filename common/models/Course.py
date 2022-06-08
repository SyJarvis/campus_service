# coding: utf-8
from application import db



class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True, info='id')
    cno = db.Column(db.String(8, 'utf8mb4_general_ci'), nullable=False, unique=True, info='课程编号')
    cname = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, info='课程名称')
    credit = db.Column(db.Integer, info='学分')
    cours = db.Column(db.Integer, info='学时')
    attribute = db.Column(db.String(5, 'utf8mb4_general_ci'), info='课程属性')
