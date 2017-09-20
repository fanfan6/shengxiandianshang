# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('txuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddr',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uconsignee',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(max_length=11, default=''),
        ),
    ]
