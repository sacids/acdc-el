# Generated by Django 2.0.9 on 2020-07-31 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20200728_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='course_meta',
            name='crs',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='crs',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Course_meta',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]
