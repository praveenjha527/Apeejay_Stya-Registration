# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20160220_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='courses',
        ),
        migrations.AddField(
            model_name='course_details',
            name='faculty',
            field=models.ManyToManyField(to='registration.Faculty', null=True, blank=True),
        ),
    ]
