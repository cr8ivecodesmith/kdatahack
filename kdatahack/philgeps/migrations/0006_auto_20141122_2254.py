# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0005_auto_20141122_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='is_amp',
            field=models.IntegerField(max_length=1, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awards',
            name='is_re_award',
            field=models.IntegerField(max_length=1, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awards',
            name='is_short_list',
            field=models.IntegerField(max_length=1, null=True),
            preserve_default=True,
        ),
    ]
