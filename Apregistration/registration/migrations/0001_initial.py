# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Enrollment_no', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'MALE'), (b'F', b'FEMALE')])),
                ('Mobile_no', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('Father_Name', models.CharField(max_length=100)),
                ('Father_mobile', models.CharField(max_length=100)),
                ('Mother_name', models.CharField(max_length=100)),
                ('Mother_mobile', models.CharField(max_length=100)),
                ('Degree', models.CharField(max_length=100)),
                ('Session', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
