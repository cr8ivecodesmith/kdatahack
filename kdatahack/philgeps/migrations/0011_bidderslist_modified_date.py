# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0010_auto_20141122_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidderslist',
            name='modified_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
