# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('philgeps', '0016_auto_20141122_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidinformation',
            name='approved_budget',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='client_agency_org_id',
            field=models.ForeignKey(related_name='client_bid_information', to_field=b'org_id', to='philgeps.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='closing_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='creation_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='modified_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='org_id',
            field=models.ForeignKey(related_name='bid_information', to_field=b'org_id', to='philgeps.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='pre_bid_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='procuring_entity_org_id',
            field=models.ForeignKey(related_name='procuring_bid_information', to_field=b'org_id', to='philgeps.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='publish_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='ref_no',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='stage',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bidinformation',
            name='stage2_ref_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
