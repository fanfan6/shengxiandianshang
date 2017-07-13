from django.db import models


# Create your models here.
class CartInfo(models.Model):
    goods = models.ForeignKey('txgoods.GoodsInfo')
    user = models.ForeignKey('txuser.UserInfo')
    count = models.IntegerField()
