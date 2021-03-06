# Generated by Django 4.0.4 on 2022-05-07 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacher_is_active'),
        ('base', '0006_statistics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statistics',
            options={'verbose_name_plural': 'Total statistics'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='number_of_students',
        ),
        migrations.CreateModel(
            name='TeacherStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_courses', models.ManyToManyField(to='base.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]
