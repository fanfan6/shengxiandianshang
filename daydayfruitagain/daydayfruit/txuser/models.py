# coding=utf-8
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=10)     # name
    upwd = models.CharField(max_length=40)      # password
    umail = models.CharField(max_length=20)     # email
    uconsignee = models.CharField(default='', max_length=10)     # consignee 收货人
    uphone = models.CharField(default='', max_length=11)    # phone number
    uaddr = models.CharField(default='', max_length=100)     # address
