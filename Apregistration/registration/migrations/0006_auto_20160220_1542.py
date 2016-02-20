# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20160220_1528'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='semester_wise_registration',
            unique_together=set([('student', 'University_Sem')]),
        ),
    ]
