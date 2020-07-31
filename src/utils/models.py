from django.db import models
from authtools.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from _datetime import timedelta
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class BaseModel(models.Model):
    created_on      = models.DateTimeField(auto_now_add=True, editable=False)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1)

class Meta:
    abstract=True # Set this model as Abstract

class categories(models.Model):

    title           = models.CharField(max_length=100)

    def __str__(self):
        return self.title if self.title else self.pk
    
    class Meta:
        db_table = 'el_categories'
        managed = True

class el_path(models.Model):

    created_on      = models.DateTimeField(auto_now_add=True, editable=False)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1)

    sort_order      = models.PositiveIntegerField(default=0)
    category        = models.ForeignKey('categories', on_delete=models.SET_NULL,null=True)
    title           = models.CharField(max_length=300)
    byline          = models.CharField(max_length=300)
    description     = models.TextField(blank=True, null=True)
    slug            = models.SlugField()
    photo           = models.ImageField(upload_to='course/photos')
    featured        = models.BooleanField(default=False)


    def __str__(self):
        return self.title if self.title else self.pk

    def get_slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('course:course_detail', kwargs={'pk': self.pk, 'slug': self.get_slug()})
    
    class Meta:
        db_table = 'el_paths'
        managed = True

class el_intake(models.Model):
    
    title           = models.CharField(max_length=300)
    slug            = models.SlugField()
    el_path         = models.ForeignKey('el_path', on_delete=models.CASCADE)
    instructor      = models.ForeignKey(User, related_name='path_instructor',on_delete=models.PROTECT)
    max_students    = models.PositiveIntegerField(default=0)
    start_date      = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_date        = models.DateTimeField(auto_now=False, auto_now_add=True)

    created_on      = models.DateTimeField(auto_now_add=True, editable=False)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_intakes'
        managed = True

class Section(models.Model):
    
    title           = models.CharField(max_length=300)
    slug            = models.SlugField()
    sort_order      = models.PositiveIntegerField(default=0)
    el_path         = models.ForeignKey('el_path', on_delete=models.CASCADE)
    publish         = models.BooleanField(default=True)

    created_on      = models.DateTimeField(auto_now_add=True, editable=False)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_sections'
        managed = True


class lessons(models.Model):

    title           = models.CharField(max_length=300)
    slug            = models.SlugField()
    description     = models.TextField(blank=True, null=True)
    prerequisite    = models.ForeignKey('lessons', on_delete=models.SET_NULL, blank=True, null=True)
    content         = models.FileField(upload_to='course/lessons/videos', max_length=100)
    el_path         = models.ForeignKey('Section', on_delete=models.CASCADE)
    duration        = models.DurationField(timedelta())
    sort_order      = models.PositiveIntegerField(default=0)

    created_on      = models.DateTimeField(auto_now_add=True, editable=False)
    created_by      = models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1)

    def __str__(self):
        return self.title if self.title else self.pk

    class Meta:
        db_table = 'el_lessons'
        managed = True
