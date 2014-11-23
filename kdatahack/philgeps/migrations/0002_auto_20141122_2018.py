# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='zip_code',
            field=models.CharField(max_length=2048, blank=True),
            preserve_default=True,
        ),
    ]
