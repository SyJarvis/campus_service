# -*- coding: UTF-8 -*-
# @Time     : 2022/6/9 15:40
# @Author   : Runke Zhong
# @Software : PyCharm



from flask import Blueprint, g, jsonify

route_api = Blueprint('api_page', __name__)

from web.controllers.api.Member import *
from web.controllers.api.PunchIn import *
from web.controllers.api.My import *


@route_api.route("/")
def index():
    return jsonify({"code": 200, "msg": "OK"})