# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0006_auto_20141122_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='awardee_id',
            field=models.ForeignKey(to='philgeps.Organization', to_field=b'org_id', null=True),
            preserve_default=True,
        ),
    ]
