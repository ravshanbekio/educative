# Generated by Django 4.0.4 on 2022-05-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
