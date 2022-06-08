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



class Mark(db.Model):
    __tablename__ = 'mark'

    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.ForeignKey('students.uid', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, info='学生id')
    cno_id = db.Column(db.ForeignKey('course.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, info='课程id')
    score = db.Column(db.Numeric(4, 2), info='成绩')
    upadted_time = db.Column(db.DateTime, info='更新时间')
    created_time = db.Column(db.DateTime, info='插入时间')

    cno = db.relationship('Course', primaryjoin='Mark.cno_id == Course.id', backref='marks')
    stu = db.relationship('Student', primaryjoin='Mark.stu_id == Student.uid', backref='marks')



class Student(db.Model):
    __tablename__ = 'students'

    uid = db.Column(db.Integer, primary_key=True, info='id')
    stu_num = db.Column(db.String(15, 'utf8_general_ci'), unique=True, info='学号')
    name = db.Column(db.String(10, 'utf8_general_ci'), nullable=False, info='姓名')
    grade = db.Column(db.String(4, 'utf8_general_ci'), info='年级')
    gender = db.Column(db.Enum('男', '女', '保密'), server_default=db.FetchedValue(), info='性别')
    age = db.Column(db.Integer, info='年龄')
    birth = db.Column(db.Date, info='出生日期')
    major = db.Column(db.Integer, info='专业id')
    _class = db.Column('class', db.Integer, info='班级id')
    people_id = db.Column(db.String(18, 'utf8_general_ci'), info='身份证号码')
    adm_date = db.Column(db.Date)
    nation = db.Column(db.String(5, 'utf8_general_ci'), info='民族')
    tel = db.Column(db.String(11, 'utf8_general_ci'), nullable=False, info='手机号码')
    address = db.Column(db.String(100, 'utf8_general_ci'), info='家庭地址')
    politics = db.Column(db.Enum('团员', '群众', '共产党员'), info='政治面貌')
    native_place = db.Column(db.String(20, 'utf8_general_ci'), info='籍贯')
    dorm_id = db.Column(db.Integer)
    registered_residence = db.Column(db.String(100, 'utf8_general_ci'), info='户籍地')

