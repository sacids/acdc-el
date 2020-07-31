# Generated by Django 2.0.9 on 2020-07-31 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20200731_1054'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0002_auto_20200730_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to='course/lessons/attachmnts')),
                ('table_name', models.CharField(max_length=300, null=True)),
                ('table_id', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'el_attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('publish', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('table_name', models.CharField(max_length=300, null=True)),
                ('table_id', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'el_announcements',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('publish', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('table_name', models.CharField(max_length=300, null=True)),
                ('table_id', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'el_discussions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('publish', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('table_name', models.CharField(max_length=300, null=True)),
                ('table_id', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'el_feedbacks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('publish', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('table_name', models.CharField(max_length=300, null=True)),
                ('table_id', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'el_notes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.PositiveIntegerField(default=0)),
                ('publish', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('table_name', models.CharField(max_length=300, null=True)),
                ('table_id', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'el_ratings',
                'managed': True,
            },
        ),
        migrations.RenameModel(
            old_name='categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='el_intake',
            new_name='ElIntake',
        ),
        migrations.RenameModel(
            old_name='el_path',
            new_name='ElPath',
        ),
        migrations.RemoveField(
            model_name='basemodel',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='lessons',
            name='prerequisite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='utils.Lessons'),
        ),
        migrations.DeleteModel(
            name='BaseModel',
        ),
    ]
