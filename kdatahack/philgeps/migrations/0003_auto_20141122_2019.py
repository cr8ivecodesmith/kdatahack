# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0002_auto_20141122_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='modified_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_reg_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
