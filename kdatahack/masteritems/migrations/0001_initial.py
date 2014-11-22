# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=2048, blank=True)),
                ('uom', models.CharField(max_length=2048, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
