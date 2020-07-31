from django.shortcuts import render
from django.core.paginator import Paginator
from utils.models import *
from django.views import generic
from django.contrib.auth.models import User

# Create your views here.

class PathListView(generic.ListView):
    model                   = ElPath
    context_object_name     = 'course_list'
    #template_name           = "course_list.html"
    paginate_by             = 8

    def get_template_names(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return "my_course_list.html"
        else:
            return "course_list.html"

    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return ElPath.objects.select_related('category').filter(category=self.kwargs['category_id']).order_by('-created_on')
        else:
            return ElPath.objects.select_related('category').all().order_by('-created_on')

class PathDetailView(generic.DetailView):
    model                   = ElPath
    context_object_name     = 'course'
    template_name           = "course_detail.html"

    def get_template_names(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return "my_course_detail.html"
        else:
            return "course_detail.html"
    
    def get_context_data(self, **kwargs):
            course_id           = self.kwargs['pk']
            context             = super(PathDetailView, self).get_context_data(**kwargs)
            context['lessons']  = Lesson.objects.filter(crs_id=course_id)
            context['featured_courses'] = el_path.objects.filter(featured=True)
            return context

