# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0003_auto_20151028_0425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlbank',
            old_name='short_url',
            new_name='short',
        ),
    ]
