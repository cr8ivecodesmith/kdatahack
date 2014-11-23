# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0011_bidderslist_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidlineitem',
            name='modified_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidlineitem',
            name='ref_id',
            field=models.ForeignKey(to='philgeps.BidInformation', to_field=b'ref_id', null=True),
            preserve_default=True,
        ),
    ]
