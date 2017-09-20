# coding=utf-8
from django.shortcuts import render, redirect
from .models import UserInfo
from hashlib import sha1
from django.http import JsonResponse
from .user_decorators import userislogin
from txgoods.models import GoodsInfo
# import datetime


# Create your views here.
def register(request):
    # '''注册界面 for register'''
    context = {'title': '注册'}
    return render(request, 'txuser/register.html', context)


def register_handle(request):
    # 注册验证 获取表单信息
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uemail = post.get('user_email')

    # 写入数据库
    user = UserInfo()
    user.uname = uname

    sha1_pwd = sha1()
    sha1_pwd.update(upwd.encode('utf-8'))
    upwd = sha1_pwd.hexdigest()

    user.upwd = upwd
    user.umail = uemail
    user.save()
    return redirect('/user/login/')


def register_valid(request):
    uname = request.GET.get('uname')
    data = UserInfo.objects.filter(uname=uname).count()
    context = {'ivalid': data}
    return JsonResponse(context)


def login(request):
    # '''登录界面 for login'''
    uname = request.COOKIES.get('uname', '')    # 获取cookie用户名，默认为空
    context = {'title': '登录', 'uname': uname}
    return render(request, 'txuser/login.html', context)


def login_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    umark = post.get('user_mark', 0)        # 默认为0

    sha1_pwd = sha1()
    sha1_pwd.update(upwd.encode('utf-8'))
    upwds = sha1_pwd.hexdigest()

    context = {'title': '登录', 'uname': uname, 'upwd': upwd}
    result = UserInfo.objects.filter(uname=uname)
    if result:
        if result[0].upwd == upwds:
            # login success

            # Renenber user_name 记住用户名
            response = redirect(request.session.get('url_path', '/'))
            request.session['uid'] = result[0].id
            request.session['uname'] = result[0].uname
            if umark == '1':        # 特别注意，此为字符串格式
                response.set_cookie('uname', uname, max_age=60*60*24*14)
                # ,  expires=datetime.datetime.now()+datetime.timedelta(days=14)
            # context['title'] = '主页'
            return response
        else:
            context['error_name'] = '用户名或密码错误'
            return render(request, 'txuser/login.html', context)
    else:
        # username not found
        context['error_name'] = '用户名或密码错误'
        return render(request, 'txuser/login.html', context)


@userislogin
def order(request):
    context = {'title': '订单'}
    return render(request, 'txuser/order.html',context)


@userislogin
def site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        post = request.POST
        uconsignee = post.get('uconsignee')
        uaddr = post.get('uaddrs')
        umail = post.get('user_email')
        uphone = post.get('user_phone')

        user.uconsignee = uconsignee
        user.uaddr = uaddr
        user.umail = umail
        user.uphone = uphone
        user.save()
    else:
        # GET请求
        pass
    context = {'title': '地址', 'user': user}
    return render(request, 'txuser/site.html', context)


@userislogin
def info(request):
    user = UserInfo.objects.get(pk=request.session['uid'])

    # 查询最近浏览记录
    ids = request.COOKIES.get('goods_ids', '').split(',')
    glist = []
    for id in ids:
        glist.append(GoodsInfo.objects.get(id=id))

    context = {'title': '个人中心', 'user': user, 'goodslist': glist}
    return render(request, 'txuser/info.html', context)


def logout(request):
    request.session.flush()
    return render(request, 'txuser/login.html')


def islogin(request):
    result = 0
    if request.session.has_key('uid'):
        result = 1
    return JsonResponse({'islogin': result})
