# -*- coding: UTF-8 -*-
# @Time     : 2022/6/7 21:39
# @Author   : Runke Zhong
# @Software : PyCharm
from web.controllers.index import route_index
from application import app

app.register_blueprint(route_index, url_prefix='/')