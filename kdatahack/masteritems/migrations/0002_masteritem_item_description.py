# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masteritems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masteritem',
            name='item_description',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
