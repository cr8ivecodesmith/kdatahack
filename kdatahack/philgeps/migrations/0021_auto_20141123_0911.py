# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0020_auto_20141123_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidinformation',
            name='ref_id',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
