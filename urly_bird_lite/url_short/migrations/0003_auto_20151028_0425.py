# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0002_auto_20151028_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlbank',
            name='short_url',
            field=models.CharField(max_length=50, blank=True, unique=True),
        ),
    ]
