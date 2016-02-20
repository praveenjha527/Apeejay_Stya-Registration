# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20160220_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_details',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='historicalcourse_details',
            name='content_type',
        ),
        migrations.AddField(
            model_name='course_details',
            name='pre_requisite',
            field=models.ManyToManyField(related_name='_pre_requisite_+', to='registration.course_details'),
        ),
    ]
