from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Course, Lesson, Course_meta
from django.views import generic

# Create your views here.
class CourseListView(generic.ListView):
    model           = Course
    template_name   = "course_list.html"
    paginate_by     = 8

    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return Course.objects.filter(category=self.kwargs['category_id']).order_by('-created_on')
        else:
            return Course.objects.all().order_by('-created_on')
        
    
class CourseDetailView(generic.DetailView):
    model           = Course
    template_name   = "course_detail.html"
    
    def get_context_data(self, **kwargs):
            course_id           = self.kwargs['pk']
            context             = super(CourseDetailView, self).get_context_data(**kwargs)
            context['lessons']  = Lesson.objects.filter(crs_id=course_id)
            context['featured_courses'] = Course.objects.filter(featured=True)
            context['course_meta']      = Course_meta.objects.filter(crs_id=course_id)
            return context

