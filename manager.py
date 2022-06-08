# -*- coding: UTF-8 -*-
# @Time     : 2022/6/7 21:40
# @Author   : Runke Zhong
# @Software : PyCharm

from flask_script import Server
from application import app, manage
import www
from application import db
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

manage.add_command("runserver", Server(host="127.0.0.1", port=app.config['SERVER_PORT']))
manage.add_command("db", MigrateCommand)


def main():
    manage.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
