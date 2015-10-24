# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='course_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=1, choices=[(b'D', b'DEGREE'), (b'O', b'OPEN'), (b'C', b'CORE')])),
                ('title', models.CharField(max_length=100)),
                ('University_sem', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Course Details',
                'verbose_name_plural': 'Course_Details',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Designation', models.CharField(max_length=4, choices=[(b'HOD', b'Head of Department'), (b'D', b'DEAN'), (b'AP', b'Associate-Professor'), (b'L', b'Lab-Assistant')])),
                ('Department', models.CharField(max_length=100)),
                ('faculty_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
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
                ('Mentor', models.ForeignKey(to='registration.Faculty')),
                ('course', models.ForeignKey(default=None, to='registration.course_details', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.AddField(
            model_name='course_details',
            name='faculty',
            field=models.ForeignKey(to='registration.Faculty'),
        ),
    ]
