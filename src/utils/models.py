from django.db import models
from authtools.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from _datetime import timedelta
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_categories'
        managed = True


class ElPath(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=1)
    sort_order = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300)
    byline = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    photo = models.ImageField(upload_to='course/photos')
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title if self.title else self.pk

    def get_slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('course:course_detail', kwargs={'pk': self.pk, 'slug': self.get_slug()})
    
    class Meta:
        db_table = 'el_paths'
        managed = True


class ElIntake(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    el_path = models.ForeignKey(ElPath, on_delete=models.CASCADE)
    instructor = models.ForeignKey(
        User, related_name='path_instructor', on_delete=models.PROTECT)
    max_students = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_intakes'
        managed = True


class Section(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    sort_order = models.PositiveIntegerField(default=0)
    el_path = models.ForeignKey(ElPath, on_delete=models.CASCADE)
    publish = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_sections'
        managed = True


class Lessons(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    prerequisite = models.ForeignKey(
        'Lessons', on_delete=models.DO_NOTHING, blank=True, null=True)
    content = models.FileField(
        upload_to='course/lessons/videos', max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    duration = models.DurationField(timedelta())
    sort_order = models.PositiveIntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_lessons'
        managed = True


# announcements
class Announcement(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    publish = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    table_name = models.CharField(max_length=300, null=True)
    table_id = models.PositiveIntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_announcements'
        managed = True


# feedback
class Feedback(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    publish = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    table_name = models.CharField(max_length=300, null=True)
    table_id = models.PositiveIntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_feedbacks'
        managed = True


# discussions
class Discussion(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    publish = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    table_name = models.CharField(max_length=300, null=True)
    table_id = models.PositiveIntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_discussions'
        managed = True


# ratings
class Rating(models.Model):
    vote = models.PositiveIntegerField(default=0)
    publish = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    table_name = models.CharField(max_length=300, null=True)
    table_id = models.PositiveIntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        db_table = 'el_ratings'
        managed = True


# notes
class Note(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    publish = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    table_name = models.CharField(max_length=300, null=True)
    table_id = models.PositiveIntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_notes'
        managed = True


# Attachment
class Attachment(models.Model):
    content = models.FileField(
        upload_to='course/lessons/attachmnts', max_length=100)

    table_name = models.CharField(max_length=300, null=True)
    table_id = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'el_attachments'
        managed = False
