# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20151024_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=1, choices=[(b'D', b'DEGREE'), (b'O', b'OPEN'), (b'C', b'CORE')])),
                ('title', models.CharField(max_length=100)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
