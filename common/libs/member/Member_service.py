# -*- coding: UTF-8 -*-
# @Time     : 2022/6/9 15:51
# @Author   : Runke Zhong
# @Software : PyCharm
import json
import random, string
from application import app
from flask import current_app
import requests, hashlib


class MemberService():

    @staticmethod
    def geneAuthCode(member_info):
        m = hashlib.md5()
        str = "%s-%s-%s" % (member_info.id, member_info.salt, member_info.status)
        m.update(str.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def geneSalt(length=8):
        salt_list = [random.choice(string.digits+string.ascii_letters) for i in range(length)]
        return "".join(salt_list)

    @staticmethod
    def getWeChatOpenId(code):

        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code"\
            .format(app.config['CAMPUS_SERVICE_APP']['appid'], app.config['CAMPUS_SERVICE_APP']['appkey'], code)

        try:
            r = requests.get(url)
        except Exception as e:
            current_app.logger.info(e)

#         {'session_key': '2vTDqTQJ/4dr7L24O0zWKQ==', 'openid': 'oesTl5ZSMGOOY6lvlZijsxmPtowU'}

        openid = None
        res = json.loads(r.text)
        if 'openid' in res:
            openid = res['openid']
        return openid