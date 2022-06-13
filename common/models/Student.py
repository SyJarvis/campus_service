# coding: utf-8
from application import db



class Student(db.Model):
    __tablename__ = 'students'

    uid = db.Column(db.Integer, primary_key=True, info='id')
    stu_num = db.Column(db.String(15, 'utf8_general_ci'), info='??')
    name = db.Column(db.String(10, 'utf8_general_ci'), nullable=False, info='??')
    grade = db.Column(db.String(4, 'utf8_general_ci'), info='??')
    gender = db.Column(db.Enum('男', '女', '保密'), server_default=db.FetchedValue(), info='??')
    age = db.Column(db.Integer, info='??')
    birth = db.Column(db.Date, info='????')
    major = db.Column(db.Integer, info='??id')
    class_id = db.Column(db.Integer, info='??id')
    people_id = db.Column(db.String(18, 'utf8_general_ci'), info='?????')
    adm_date = db.Column(db.Date)
    nation = db.Column(db.String(5, 'utf8_general_ci'), info='??')
    tel = db.Column(db.String(11, 'utf8_general_ci'), nullable=False, info='????')
    address = db.Column(db.String(100, 'utf8_general_ci'), info='????')
    politics = db.Column(db.Enum('团员', '群众', '共产党员'), info='????')
    native_place = db.Column(db.String(20, 'utf8_general_ci'), info='??')
    dorm_id = db.Column(db.Integer)
    registered_residence = db.Column(db.String(100, 'utf8_general_ci'), info='???')
