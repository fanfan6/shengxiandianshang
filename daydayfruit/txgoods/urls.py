from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.goodslist),
    url(r'^(\d+)/$', views.detail),
]
