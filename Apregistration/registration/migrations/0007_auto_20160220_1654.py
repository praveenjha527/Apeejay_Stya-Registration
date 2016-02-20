# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20160220_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semester_wise_registration',
            options={'verbose_name': 'Course_Registration', 'verbose_name_plural': 'Course_Registrations'},
        ),
    ]
