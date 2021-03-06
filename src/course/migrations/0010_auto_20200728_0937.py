# Generated by Django 2.0.9 on 2020-07-28 09:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0009_course_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_meta',
            name='instructor',
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.DurationField(default=datetime.timedelta),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='instructor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='max_students',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='course_meta',
            name='crs',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]
