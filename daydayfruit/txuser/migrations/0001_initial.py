# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=10)),
                ('upwd', models.CharField(max_length=40)),
                ('umail', models.CharField(max_length=20)),
                ('uconsignee', models.CharField(max_length=10)),
                ('uphone', models.CharField(max_length=11)),
                ('uaddr', models.CharField(max_length=100)),
            ],
        ),
    ]
