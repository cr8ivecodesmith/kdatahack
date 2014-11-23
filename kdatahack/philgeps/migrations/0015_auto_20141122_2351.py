# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0014_auto_20141122_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidlineitem',
            name='item_description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
