# Generated by Django 5.0.3 on 2024-03-06 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otpa', '0006_alter_student_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
    ]