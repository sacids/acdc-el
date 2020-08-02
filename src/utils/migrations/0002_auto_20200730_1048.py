# Generated by Django 2.0.9 on 2020-07-30 10:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'el_categories',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='el_intake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('max_students', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'el_intakes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='el_path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=300)),
                ('byline', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('photo', models.ImageField(upload_to='course/photos')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.categories')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'el_paths',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.FileField(upload_to='course/lessons/videos')),
                ('duration', models.DurationField(verbose_name=datetime.timedelta(0))),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'el_lessons',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('publish', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('el_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.el_path')),
            ],
            options={
                'db_table': 'el_sections',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lessons',
            name='el_path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Section'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='prerequisite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.lessons'),
        ),
        migrations.AddField(
            model_name='el_intake',
            name='el_path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.el_path'),
        ),
        migrations.AddField(
            model_name='el_intake',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='path_instructor', to=settings.AUTH_USER_MODEL),
        ),
    ]