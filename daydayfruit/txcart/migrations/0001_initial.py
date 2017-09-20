# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('txgoods', '0001_initial'),
        ('txuser', '0002_auto_20170710_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='txgoods.GoodsInfo')),
                ('user', models.ForeignKey(to='txuser.UserInfo')),
            ],
        ),
    ]
