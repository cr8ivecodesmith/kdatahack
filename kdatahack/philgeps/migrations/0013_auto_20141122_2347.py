# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0012_auto_20141122_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidlineitem',
            name='line_item_id',
            field=models.PositiveIntegerField(unique=True, null=True),
            preserve_default=True,
        ),
    ]
