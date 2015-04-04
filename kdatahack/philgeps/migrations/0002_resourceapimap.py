# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('philgeps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceAPIMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_endpoint', models.URLField()),
                ('source_model', models.OneToOneField(to='contenttypes.ContentType')),
            ],
            bases=(models.Model, core.models.SelfAwareModelMixin),
        ),
    ]
