# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0013_auto_20141122_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidlineitem',
            name='item_name',
            field=models.CharField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
    ]
