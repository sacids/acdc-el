# Generated by Django 2.0.9 on 2020-07-23 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200723_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='course_id',
            new_name='course_pk',
        ),
    ]
