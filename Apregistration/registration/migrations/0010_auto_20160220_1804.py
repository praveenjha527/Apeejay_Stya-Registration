# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_auto_20160220_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_details',
            name='pre_requisite',
            field=models.ManyToManyField(related_name='_pre_requisite_+', null=True, to='registration.course_details', blank=True),
        ),
    ]
