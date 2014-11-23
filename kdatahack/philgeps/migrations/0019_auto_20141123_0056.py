# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0018_auto_20141123_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidinformation',
            name='ref_no',
            field=models.CharField(max_length=2048, blank=True),
            preserve_default=True,
        ),
    ]
