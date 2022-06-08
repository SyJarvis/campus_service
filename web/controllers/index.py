# -*- coding: UTF-8 -*-
# @Time     : 2022/6/7 21:49
# @Author   : Runke Zhong
# @Software : PyCharm


from flask import Blueprint
from flask import current_app

route_index = Blueprint("index_page", __name__)


@route_index.route("/")
def index():
    current_app.logger.error("sss")

    return "HelloWolrd"