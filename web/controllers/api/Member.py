# -*- coding: UTF-8 -*-
# @Time     : 2022/6/9 15:41
# @Author   : Runke Zhong
# @Software : PyCharm


from web.controllers.api import route_api
from application import db
from flask import request, jsonify, g
from common.libs.response_code import RET
from common.libs.member.Member_service import MemberService
from common.models.Member import Member
from common.models.OauthMemberBind import OauthMemberBind
from common.libs.Helper import getCurrentDate
from common.models.Student import Student
from common.models.ClassTable import ClassTable
from common.models.User import User
from flask import current_app



@route_api.route('/member/login', methods=['GET', 'POST'])
def login():
    current_app.logger.info(request.remote_addr)
    resp = {'code':RET.OK, 'msg':'操作成功', 'data':{}}
    req = request.values
    print("=============================================")
    print(req)
    code = req['code'] if 'code' in req else ''
    current_app.logger.info(req)
    if not code or len(code) < 1:
        resp['code'] = RET.PARAMERR
        resp['msg'] = '参数错误'
        return jsonify(resp)

    openid = MemberService.getWeChatOpenId(code)
    if openid is None:
        resp['code'] = RET.PARAMERR
        resp['msg'] = '参数错误'
        return jsonify(resp)
    current_app.logger.info(openid)

    nickname = req['nickName'] if 'nickName' in req else ''
    sex = req['gender'] if 'gender' in req else 0
    avatar = req['avatarUrl'] if 'avatarUrl' in req else ''
    print(nickname)
    print(sex)
    print(avatar)
    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()

   
    if not bind_info:
        current_app.logger.info("not bind_info")
        member = Member()
        member.nickname = nickname
        member.mobile = ''
        member.reg_ip = request.remote_addr
        member.sex = sex
        member.avatar = avatar
        member.salt = MemberService.geneSalt()
        member.status = 1
        member.updated_time = getCurrentDate()
        member.created_time = getCurrentDate()
        db.session.add(member)
        db.session.commit()

        member_bind = OauthMemberBind()
        member_bind.member_id = member.id
        member_bind.client_type = 'weixin'
        member_bind.unionid = ''
        member_bind.type = 1
        member_bind.openid = openid
        member_bind.extra = ''
        member_bind.updated_time = getCurrentDate()
        member_bind.created_time = getCurrentDate()
        db.session.add(member_bind)
        db.session.commit()

        bind_info = member_bind
        current_app.logger.info("database is ok")

    member_info = Member.query.filter_by(id=bind_info.member_id).first()
    token = "%s#%s" % (MemberService.geneAuthCode(member_info), member_info.id)
    current_app.logger.info("have bind_info")
    resp['data'] = {'token':token}
    return jsonify(resp)


@route_api.route("/member/check-reg", methods=['GET', 'POST'])
def checkReg():
    # 接收参数
    resp = {'code': RET.OK, 'msg':'操作成功', 'data':{}}
    req = request.values
    print(req)
    code = req['code'] if 'code' in req else ''

    if not code or len(code) < 1:
        resp['code'] = RET.PARAMERR
        resp['msg'] = 'error'
        return jsonify(resp)

    openid = MemberService.getWeChatOpenId(code)
    if openid is None:
        resp['code'] = RET.DATAERR
        resp['msg'] = '未绑定'
        return jsonify(resp)

    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()
    if not bind_info:
        resp['code'] = RET.USERERR
        resp['msg'] = '未绑定2'
        return jsonify(resp)

    # 查询绑定信息
    member_info = Member.query.filter_by(id=bind_info.member_id).first()
    if not member_info:
        resp['code'] = RET.USERERR
        resp['msg'] = '未查询到绑定信息'
        return jsonify(resp)

    user_info = User.query.filter_by(member_id=member_info.id).first()
    if not user_info:
        resp['code'] = RET.NOTBINDUSER
        resp['msg'] = '没有绑定学生信息'
        return jsonify(resp)

    token = "%s#%s" % (MemberService.geneAuthCode(member_info), member_info.id)
    resp['data'] = {'token': token}
    return jsonify(resp)


@route_api.route('/member/auth_bind', methods=['POST'])
def AuthBind():
    resp = {'code':RET.OK, 'msg':'操作成功', 'data':{}}
    req = request.values
    token = request.headers['Authorization']

    print(req)
    print('=========================')
    print('token：', token)
    school_name = req['school'] if 'school' in req else ''
    college_name = req['college'] if 'college' in req else ''
    class_name = req['class'] if 'class' in req else ''
    name = req['name'] if 'name' in req else ''
    stu_num = req['StuNum'] if 'StuNum' in req else ''
    if not all([school_name, college_name, class_name, name, stu_num]):
        resp['code'] = RET.PARAMERR
        resp['msg'] = '参数不完整'
        return jsonify(resp)

    class_info = ClassTable.query.filter_by(name=class_name).first()
    print("============class_info================")
    print(class_info)
    user_info = User.query.filter_by(name=name, stu_num=stu_num).first()
    if user_info:
        resp['code'] = RET.OK
        resp['msg'] = '已存在'
        print(resp)
        return jsonify(resp)

    stu_info = Student.query.filter_by(name=name, stu_num=stu_num).first()
    if not stu_info:
        resp['code'] = RET.PARAMERR
        resp['msg'] = '没有此学生信息, 请重试'
        return jsonify(resp)
    else:
        member_id = int(token.split("#")[1])
        user_info = User()
        user_info.stu_num = stu_num
        user_info.name = name
        user_info.member_id = member_id
        user_info.class_id = class_info.id
        user_info.status = 1
        user_info.created_time = getCurrentDate()
        user_info.updated_time = getCurrentDate()

        db.session.add(user_info)
        db.session.commit()
    resp['data']['token'] = token
    return jsonify(resp)