# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20160220_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_details',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='historicalcourse_details',
            name='faculty',
        ),
        migrations.AddField(
            model_name='faculty',
            name='courses',
            field=models.ManyToManyField(to='registration.course_details', null=True, blank=True),
        ),
    ]
