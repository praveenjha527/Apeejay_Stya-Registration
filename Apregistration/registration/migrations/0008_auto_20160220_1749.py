# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('registration', '0007_auto_20160220_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_details',
            name='pre_requisite',
        ),
        migrations.RemoveField(
            model_name='historicalcourse_details',
            name='pre_requisite',
        ),
        migrations.AddField(
            model_name='course_details',
            name='content_type',
            field=models.ForeignKey(default=int(str(23)), to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalcourse_details',
            name='content_type',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='contenttypes.ContentType', null=True),
        ),
    ]
