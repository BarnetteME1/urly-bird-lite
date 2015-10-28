# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urlbank',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='urlbank',
            name='created',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='urlbank',
            unique_together=set([('url', 'user')]),
        ),
    ]
