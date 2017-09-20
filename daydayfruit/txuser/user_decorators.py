# coding=utf-8
from django.shortcuts import redirect


# 装饰器，未登录者禁止访问某些模块
def userislogin(func):
    def func1(request, *args, **kwargs):
        if 'uid' in request.session:
            return func(request,  *args, **kwargs)
        else:
            return redirect('/user/login/')
    return func1

