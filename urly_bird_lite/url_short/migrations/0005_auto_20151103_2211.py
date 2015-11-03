# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('url_short', '0004_auto_20151028_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickCount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('clicked', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='urlbank',
            name='short',
            field=models.CharField(blank=True, unique=True, max_length=32),
        ),
        migrations.AddField(
            model_name='clickcount',
            name='link',
            field=models.ForeignKey(to='url_short.UrlBank'),
        ),
        migrations.AddField(
            model_name='clickcount',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
