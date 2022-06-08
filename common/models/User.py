# -*- coding: UTF-8 -*-
# @Time     : 2022/6/8 17:20
# @Author   : Runke Zhong
# @Software : PyCharm


from application import db

class User(db.Model):


    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, info='id')
    tea_num = db.Column(db.String(20, 'utf8mb4_general_ci'), unique=True, info='编号')
    name = db.Column(db.String(20, 'utf8mb4_general_ci'), info='姓名')
    gender = db.Column(db.Enum('男', '女'), info='性别')
    wechat_num = db.Column(db.String(50, 'utf8mb4_general_ci'), info='微信号')
    phone = db.Column(db.String(11, 'utf8mb4_general_ci'), info='手机号码')
    email = db.Column(db.String(20, 'utf8mb4_general_ci'), info='邮箱')
    updated_time = db.Column(db.DateTime, info='更新时间')
    created_time = db.Column(db.DateTime, info='插入时间')