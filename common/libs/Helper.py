# -*- coding: UTF-8 -*-
# @Time     : 2022/6/8 15:15
# @Author   : Runke Zhong
# @Software : PyCharm

from flask import render_template, g
import datetime

'''
统一渲染方法
'''

def ops_render(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)