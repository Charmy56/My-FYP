# Generated by Django 5.0.3 on 2024-03-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpa', '0005_alter_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(default='DEMOStudent', max_length=150),
        ),
    ]
