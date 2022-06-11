# -*- coding: UTF-8 -*-
# @Time     : 2022/6/7 21:49
# @Author   : Runke Zhong
# @Software : PyCharm


from flask import Blueprint
from flask import current_app
from common.libs.member.Member_service import MemberService

route_index = Blueprint("index_page", __name__)


@route_index.route("/")
def index():
    current_app.logger.error("sss")
    MemberService.getWeChatOpenId("083VxIll2yb1k94vlOml2EgFDv2VxIlF")
    return "HelloWolrd"