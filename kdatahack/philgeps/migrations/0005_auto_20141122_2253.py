# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='award_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awards',
            name='contract_end_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awards',
            name='contract_start_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awards',
            name='proceed_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awards',
            name='publish_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
