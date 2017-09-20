from django.shortcuts import render
from . import models
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    type_list = models.TypeInfo.objects.all()
    goodslist = []
    for ty_list in type_list:
        new_list = ty_list.goodsinfo_set.order_by('-id')[0:4]
        click_list = ty_list.goodsinfo_set.order_by('-gclick')[0:4]
        goodslist.append({'new_list': new_list, 'click_list': click_list, 'type_list': ty_list})
    context = {'title': '首页', 'goodslist': goodslist}
    return render(request, 'txgoods/index.html', context)


def goodslist(request, tid, pindex, orderby):
    typelist = models.TypeInfo.objects.get(pk=int(tid))
    orderby_str = '-id'
    if int(orderby) == 2:
        orderby_str = '-gprice'
    elif int(orderby) == 3:
        orderby_str = '-gclick'
    new_list = typelist.goodsinfo_set.order_by('-id')[0:2]
    glist = typelist.goodsinfo_set.order_by(orderby_str)
    # 分页
    paginator = Paginator(glist, 10)
    page = paginator.page(int(pindex))

    context = {'title': '列表', 'typelist': typelist,
               'new_list': new_list, 'page': page, 'orderby': orderby}
    return render(request, 'txgoods/list.html', context)


def detail(request, id):
    try:
        goods = models.GoodsInfo.objects.get(pk=int(id))
        # click +1
        goods.gclick += 1
        goods.save()

        # 当前商品分类对象--> 此类商品中新的两个对象
        new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        context = {'title': '详情', 'goods': goods, 'new_list': new_list}
        response = render(request, 'txgoods/detail.html', context)
        # 最近浏览
        ids = request.COOKIES.get('goods_ids', '').split(',')[:-1]
        if id in ids:
            ids.remove(id)
        ids.insert(0, id)
        if len(ids) > 5:
            ids.pop()

        response.set_cookie('goods_ids', ','.join(ids), max_age=60*60*24*7)
        return response
    except:
        return render(request, '404.html')
