# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0008_auto_20141122_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='ref_id',
            field=models.ForeignKey(to='philgeps.BidInformation', to_field=b'ref_id', null=True),
            preserve_default=True,
        ),
    ]
