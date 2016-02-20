# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_course_details_credit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='course_details',
            name='student',
            field=models.ForeignKey(default=datetime.datetime(2016, 2, 5, 7, 31, 24, 872721, tzinfo=utc), to='registration.Student'),
            preserve_default=False,
        ),
    ]
