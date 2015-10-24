# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20151024_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='Designation',
            field=models.CharField(default=datetime.datetime(2015, 10, 24, 7, 28, 8, 556901, tzinfo=utc), max_length=4, choices=[(b'HOD', b'Head of Department'), (b'D', b'DEAN'), (b'AP', b'Associate-Professor'), (b'L', b'Lab-Assistant')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Department',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
