# coding: utf-8
from application import db



class Dormitory(db.Model):
    __tablename__ = 'dormitory'

    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(10, 'utf8_general_ci'), info='区域,天河校区西区、天河校区东区')
    dorm_name = db.Column(db.String(10, 'utf8_general_ci'), info='宿舍楼名')
    dorm_no = db.Column(db.String(3, 'utf8_general_ci'), info='宿舍号')
    dorm_fee = db.Column(db.Float(10), info='宿舍费')
