# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Department', models.CharField(max_length=4, choices=[(b'HOD', b'Head of Department'), (b'D', b'DEAN'), (b'AP', b'Associate-Professor'), (b'L', b'Lab-Assistant')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='Mentor',
            field=models.ForeignKey(default=datetime.datetime(2015, 10, 24, 7, 25, 0, 781512, tzinfo=utc), to='registration.Faculty'),
            preserve_default=False,
        ),
    ]
