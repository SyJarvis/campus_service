# -*- coding: UTF-8 -*-
# @Time     : 2022/6/7 21:37
# @Author   : Runke Zhong
# @Software : PyCharm

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

class Application(Flask):

    def __init__(self, import_name, template_folder=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, static_folder=None)
        self.config.from_pyfile("config/base_setting.py")
        db.init_app(self)


root_path = os.getcwd()
db = SQLAlchemy()
app = Application("__name__", template_folder=root_path + "/web/templates")
app.root_path = root_path
manage = Manager(app)

