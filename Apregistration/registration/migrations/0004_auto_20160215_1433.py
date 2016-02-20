# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0003_auto_20160205_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historicalcourse_details',
            fields=[
                ('code', models.CharField(max_length=100, db_index=True)),
                ('type', models.CharField(max_length=1, choices=[(b'D', b'DEGREE'), (b'O', b'OPEN'), (b'C', b'CORE')])),
                ('pre_requisite', models.CharField(default=b'[]', max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('University_sem', models.CharField(max_length=100)),
                ('credit', models.IntegerField(default=None)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Course Details',
            },
        ),
        migrations.CreateModel(
            name='HistoricalFaculty',
            fields=[
                ('id', models.CharField(max_length=100, db_index=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Designation', models.CharField(max_length=4, choices=[(b'HOD', b'Head of Department'), (b'D', b'DEAN'), (b'AP', b'Associate-Professor'), (b'L', b'Lab-Assistant')])),
                ('Department', models.CharField(max_length=100)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('faculty_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Faculty',
            },
        ),
        migrations.CreateModel(
            name='HistoricalStudent',
            fields=[
                ('Enrollment_no', models.CharField(max_length=16, db_index=True)),
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
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('Mentor', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='registration.Faculty', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical student',
            },
        ),
        migrations.CreateModel(
            name='Semester_Wise_Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('University_Sem', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=3, choices=[(b'N', b'NOT-ATTEMPTED'), (b'P', b'PASS'), (b'I', b'IMPROVEMENT'), (b'R', b'RE-APPEAR')])),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='course_details',
            name='id',
        ),
        migrations.RemoveField(
            model_name='course_details',
            name='student',
        ),
        migrations.AddField(
            model_name='course_details',
            name='pre_requisite',
            field=models.CharField(default=b'[]', max_length=100),
        ),
        migrations.AlterField(
            model_name='course_details',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='historicalcourse_details',
            name='Registration',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='registration.Semester_Wise_Registration', null=True),
        ),
        migrations.AddField(
            model_name='historicalcourse_details',
            name='faculty',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='registration.Faculty', null=True),
        ),
        migrations.AddField(
            model_name='historicalcourse_details',
            name='history_user',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='course_details',
            name='Registration',
            field=models.ForeignKey(default=b'', to='registration.Semester_Wise_Registration'),
        ),
    ]
