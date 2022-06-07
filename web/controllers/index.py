# -*- coding: UTF-8 -*-
# @Time     : 2022/6/7 21:49
# @Author   : Runke Zhong
# @Software : PyCharm


from flask import Blueprint

route_index = Blueprint("index_page", __name__)


@route_index.route("/")
def index():
    return "HelloWolrd"