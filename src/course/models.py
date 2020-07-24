from django.db import models
from utils.models import BaseModel
from authtools.models import User
from datetime import datetime, timedelta
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Course(BaseModel):
    title           = models.CharField(max_length=200)
    summary         = models.TextField(max_length=500)
    description     = models.TextField()
    byline          = models.CharField(max_length=250, blank=True, null=True)
    icon            = models.CharField(max_length=50)
    image           = models.CharField(max_length=50,blank=True, null=True)
    active          = models.BooleanField()
    featured        = models.BooleanField()
    category        = models.ForeignKey('Category', related_name='course_category',on_delete=models.PROTECT)

    def __str__(self):
        return self.title if self.title else self.course_id
    
    def get_slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('course:course_detail', kwargs={'pk': self.pk, 'slug': self.get_slug()})

    class Meta:
        db_table = 'el_course'
        managed = True

class Course_meta(models.Model):

    crs             = models.ForeignKey('Course', on_delete=models.CASCADE)
    duration        = models.DurationField(default=timedelta)
    max_students    = models.IntegerField()
    instructor      = models.ForeignKey(User, related_name='instructor',on_delete=models.PROTECT)
    start_date      = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.course_meta_id

    class Meta:
        db_table    = 'el_course_meta'
        managed     = True
        verbose_name = 'Course_meta'
        verbose_name_plural = 'Course_metas'

class Lesson(BaseModel):

    crs             = models.ForeignKey('Course', on_delete=models.CASCADE)
    title           = models.CharField(max_length=250, blank=True, null=True)
    icon_font       = models.CharField(max_length=50, blank=True, null=True)
    prerequisite    = models.IntegerField(default=0)
    duration        = models.DurationField(default=timedelta)
    byline          = models.CharField(max_length=250, blank=True, null=True)
    summary         = models.TextField()
    content         = models.TextField()
    video           = models.CharField(max_length=250, blank=True, null=True)
    audio           = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else self.lesson_id

    class Meta:
        db_table    = 'el_course_lessons'
        managed     = True

class Category(models.Model):
    
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title if self.title else self.category_id

    class Meta:
        db_table    = 'el_category'