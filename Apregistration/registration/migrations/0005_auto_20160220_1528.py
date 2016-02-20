# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20160215_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_details',
            name='Registration',
        ),
        migrations.RemoveField(
            model_name='historicalcourse_details',
            name='Registration',
        ),
        migrations.AddField(
            model_name='semester_wise_registration',
            name='course',
            field=models.ManyToManyField(to='registration.course_details'),
        ),
    ]
