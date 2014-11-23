# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0007_auto_20141122_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='line_item_id',
            field=models.ForeignKey(to='philgeps.BidLineItem', to_field=b'line_item_id', null=True),
            preserve_default=True,
        ),
    ]
