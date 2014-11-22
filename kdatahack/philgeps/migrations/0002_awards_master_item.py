# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masteritems', '0002_masteritem_item_description'),
        ('philgeps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='master_item',
            field=models.ForeignKey(related_name='awards_set', blank=True, to='masteritems.MasterItem', null=True),
            preserve_default=True,
        ),
    ]
