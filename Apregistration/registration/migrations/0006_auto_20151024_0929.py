# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20151024_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='user',
            new_name='faculty_user',
        ),
    ]
