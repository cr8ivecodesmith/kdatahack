# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0009_auto_20141122_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidderslist',
            name='award_id',
            field=models.ForeignKey(to='philgeps.Awards', to_field=b'award_id', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidderslist',
            name='line_item_id',
            field=models.ForeignKey(to='philgeps.BidLineItem', to_field=b'line_item_id', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidderslist',
            name='org_id',
            field=models.ForeignKey(to='philgeps.Organization', to_field=b'org_id', null=True),
            preserve_default=True,
        ),
    ]
