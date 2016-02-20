# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20160220_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester_wise_registration',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='semester_wise_registration',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
