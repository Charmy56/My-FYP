# Generated by Django 5.0 on 2024-08-03 14:56

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpa', '0011_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('is_present', models.BooleanField(default=False)),
                ('confirmed_by_lecturer', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otpa.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otpa.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('attended', models.BooleanField(default=False)),
                ('confirmed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='otpa.lecturer')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otpa.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otpa.student')),
            ],
        ),
    ]
