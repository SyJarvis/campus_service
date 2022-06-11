# -*- coding: UTF-8 -*-
# @Time     : 2022/6/10 16:35
# @Author   : Runke Zhong
# @Software : PyCharm


from web.controllers.api import route_api
from common.libs.response_code import RET
from common.models.Member import Member
from flask import request, jsonify, g, current_app


@route_api.route("/my/info", methods=['GET', 'POST'])
def MyInfo():

    resp = {'code': RET.OK, 'msg':'操作成功', 'data':{}}
    current_app.logger.info(request.headers)
    current_app.logger.info(type(request.headers))
    print("sss")
    auth = request.headers['Authorization']
    id = auth.split('#')[1]
    member_info = Member.query.filter_by(id=id, status=1).first()
    print(member_info.nickname)
    resp['data']['nickName'] = member_info.nickname
    resp['data']['avatarUrl'] = member_info.avatar
    resp['data']['stu_num'] = '202103130000'
    resp['data']['drom_name'] = '广东工贸东4'
    return jsonify(resp)