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
            course_id                   = self.kwargs['pk']
            context                     = super(PathDetailView, self).get_context_data(**kwargs)
            context['curriculum']       = Section.objects.filter(el_path_id=course_id).prefetch_related('lesson')
            #context['featured_courses'] = ElPath.objects.filter(featured=True).prefetch_related('lesson_set')

            return context


#section
class SectionListView(generic.ListView):
    model           = Section
    template_name = "sections/lists.html"

    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return Section.objects.select_related('el_path').filter(el_path=self.kwargs['el_path_id']).order_by('-created_on')
        else:
            return Section.objects.select_related('el_path').all().order_by('-created_on')


class SectionDetailView(generic.DetailView):
    model                = Section
    template_name        = "sections/details.html"
    context_object_name  = "section"


class SectionCreateView(generic.CreateView):
    model               = Section
    template_name       = "sections/create.html"
    fields              = ('title', 'el_path', 'sort_order', 'publish',)


class SectionUpdateView(generic.UpdateView): 
    model                   = Section
    template_name           = 'sections/edit.html'
    context_object_name     = 'section'
    fields                  = ('title', 'el_path', 'sort_order', 'publish',)


class SectionDeleteView(generic.DeleteView):
    model               = Section
    template_name       = ''


#lessons
class LessonListView(generic.ListView):
    model         = Lesson
    template_name = "lessons/lists.html"

    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return Lesson.objects.select_related('section').filter(section=self.kwargs['section_id']).order_by('-created_on')
        else:
            return Lesson.objects.select_related('section').all().order_by('-created_on')


class LessonDetailView(generic.DetailView):
    model               = Lesson
    template_name       = "lessons/details.html"
    context_object_name = "lesson"


class LessonCreateView(generic.CreateView):
    model               = Lesson
    template_name       = "lessons/create.html"
    fields              = ('title', 'description', 'publish', 'prerequisite','content', 'section', 'duration', 'sort_order',)


class LessonUpdateView(generic.UpdateView):
    model               = Lesson
    template_name       = 'lessons/edit.html'
    context_object_name = 'lesson'
    fields = fields     = ('title', 'description', 'publish', 'prerequisite','content', 'section', 'duration', 'sort_order',)


class LessonDeleteView(generic.DeleteView):
    model = Lesson
    template_name = ''
