# coding: utf-8
from application import db



class ClassTable(db.Model):
    __tablename__ = 'class_table'

    id = db.Column(db.Integer, primary_key=True, info='id')
    name = db.Column(db.String(20), info='????')
    major_id = db.Column(db.ForeignKey('major.id'), index=True, info='??id')
    headmaster = db.Column(db.String(8), info='???')
    instructor = db.Column(db.String(8), info='???')
    created_time = db.Column(db.DateTime, info='????')
    updated_time = db.Column(db.DateTime, info='????')

    major = db.relationship('Major', primaryjoin='ClassTable.major_id == Major.id', backref='class_tables')



class Major(db.Model):
    __tablename__ = 'major'

    id = db.Column(db.Integer, primary_key=True, info='id')
    name = db.Column(db.String(15, 'utf8_general_ci'), unique=True, info='????')
    college = db.Column(db.Integer, info='??')
