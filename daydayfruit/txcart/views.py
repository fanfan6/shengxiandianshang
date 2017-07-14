from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from . import models
from txuser.models import UserInfo
from txuser.user_decorators import userislogin

# Create your views here.


def add(request):
    try:
        uid = request.session.get('uid')
        gid = int(request.GET.get('gid'))
        count = int(request.GET.get('count', '1'))
        print(count)

        cart = models.CartInfo.objects.filter(user_id=uid, goods_id=gid)
        if len(cart) == 1:
            cart1 = cart[0]
            # print(cart1)
            if cart1.goods.gstock < cart1.count + count:
                print(cart1.count + count)
                return JsonResponse({'isadd': 2})
            else:
                cart1.count += count
            cart1.save()
        else:
            cart = models.CartInfo()
            cart.user_id = uid
            cart.goods_id = gid
            cart.count = count
            cart.save()
        return JsonResponse({'isadd': 1})
    except:
        return JsonResponse({'isadd': 0})


def count(request):
    uid = int(request.session.get('uid'))
    count1 = models.CartInfo.objects.filter(user_id=uid).count()
    return JsonResponse({'count': count1})
