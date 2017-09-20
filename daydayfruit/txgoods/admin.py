from django.contrib import admin
from . import models


# Register your models here.
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']

admin.site.register(models.TypeInfo, TypeAdmin)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice']
    list_per_page = 15

admin.site.register(models.GoodsInfo, GoodsAdmin)
