# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0005_auto_20151103_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickcount',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='urlbank',
            name='url',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
