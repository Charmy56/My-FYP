# Generated by Django 5.0.3 on 2024-03-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpa', '0007_alter_examcard_exam_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examcard',
            name='exam_photo',
            field=models.ImageField(null=True, upload_to='exam_admin_dashboard/'),
        ),
    ]