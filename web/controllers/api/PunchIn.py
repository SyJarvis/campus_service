# -*- coding: UTF-8 -*-
# @Time     : 2022/6/10 8:47
# @Author   : Runke Zhong
# @Software : PyCharm

from web.controllers.api import route_api
from common.libs.response_code import RET
from common.models.Member import Member
from flask import jsonify, g, request
from flask import current_app


@route_api.route('/punch_in', methods=['GET', 'POST'])
def punch_card():
    '''
    打卡
    :return:
    '''
    resp = {'code': RET.OK, 'msg':'操作成功'}
    current_app.logger.info(resp)
    print("========================sssssssssssssssssssssss")
    current_app.logger.info(request.json)
    return jsonify(resp)

