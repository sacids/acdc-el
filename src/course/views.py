from django.shortcuts import render
from django.core.paginator import Paginator
from utils.models import *
from django.views import generic
from django.db.models import Count
from django.contrib.auth.models import User

# Create your views here.


class PathListView(generic.ListView):
    model = ElPath
    context_object_name = 'course_list'
    template_name = "course/list.html"
    paginate_by = 8

    # def get_template_names(self, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return "course/my_list.html"
    #     else:
    #         return "course/list.html"

    def get_context_data(self, **kwargs):
        context = super(PathListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = "Courses"
        return context

    def get_queryset(self, *args, **kwargs):
        keyword = self.request.GET.get('keyword')

        if keyword:
            return ElPath.objects.select_related('category').filter(title__contains=keyword).order_by('-created_on')
        else:
            if self.kwargs:
                return ElPath.objects.select_related('category').filter(category=self.kwargs['category_id']).order_by('-created_on')
            else:
                return ElPath.objects.select_related('category').all().order_by('-created_on')


class PathDetailView(generic.DetailView):
    model = ElPath
    context_object_name = 'course'
    #template_name           = "course_detail.html"

    def get_template_names(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            course_id = self.kwargs['pk']
            if self.isRegisterdToCourse(course_id):
                return "course/learn.html"
            else:
                return "course/view.html"
        else:
            return "course/view.html"

    def get_context_data(self, **kwargs):
        context = super(PathDetailView, self).get_context_data(**kwargs)
        course_id = self.kwargs['pk']
        lesson_id = 0

        if 'lesson_id' in self.kwargs:
            lesson_id = self.kwargs['lesson_id']
            context['somo'] = Lesson.objects.get(pk=lesson_id)

        context['lesson_id'] = lesson_id
        context['curriculum'] = Section.objects.filter(
            el_path_id=course_id).prefetch_related('lesson')
        context['featured'] = ElPath.objects.filter(featured=True)[:5]
        context['course'] = ElPath.objects.select_related(
            'category').get(pk=course_id)
        context['reg_students'] = StudentRegistration.objects.filter(
            el_path_id=course_id)
        context['intakes'] = ElIntake.objects.filter(
            el_path_id=course_id).select_related('instructor')
        context['announcements'] = Announcement.objects.filter(
            table_name="el_path", table_id=course_id)
        context['title'] = "Course details"
        return context

    def isRegisterdToCourse(self, course_id):
        if not self.request.session['reg_courses']:
            return False
        else:
            if str(course_id) in self.request.session['reg_courses']:
                return True
            else:
                return False

    def post(self, request, *args, **kwargs):
        el_intake = ElIntake.objects.get(pk=request.POST.get("intake_id"))
        el_path = ElPath.objects.get(pk=request.POST.get("path_id"))
        student = request.user

        Reg, created = StudentRegistration.objects.get_or_create(
            el_intake=el_intake, el_path=el_path, student=student)

        # save to session
        tmp = {}
        tmp[Reg.el_path_id] = model_to_dict(Reg)
        request.session['reg_courses'] = tmp

        # Write Your Logic here
        self.object = self.get_object()
        context = super(PathDetailView, self).get_context_data(**kwargs)
        context['curriculum'] = Section.objects.filter(
            el_path_id=Reg.el_path_id).prefetch_related('lesson')
        return render(request, "course/learn.html", context)

# section


class SectionListView(generic.ListView):
    model = Section
    template_name = "sections/lists.html"

    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return Section.objects.select_related('el_path').filter(el_path=self.kwargs['el_path_id']).order_by('-created_on')
        else:
            return Section.objects.select_related('el_path').all().order_by('-created_on')


class SectionDetailView(generic.DetailView):
    model = Section
    template_name = "sections/details.html"
    context_object_name = "section"


class SectionCreateView(generic.CreateView):
    model = Section
    template_name = "sections/create.html"
    fields = ('title', 'el_path', 'sort_order', 'publish',)


class SectionUpdateView(generic.UpdateView):
    model = Section
    template_name = 'sections/edit.html'
    context_object_name = 'section'
    fields = ('title', 'el_path', 'sort_order', 'publish',)


class SectionDeleteView(generic.DeleteView):
    model = Section
    template_name = ''


# lessons
class LessonListView(generic.ListView):
    model = Lesson
    template_name = "lessons/lists.html"

    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return Lesson.objects.select_related('section').filter(section=self.kwargs['section_id']).order_by('-created_on')
        else:
            return Lesson.objects.select_related('section').all().order_by('-created_on')


class LessonDetailView(generic.DetailView):
    model = Lesson
    template_name = "lessons/details.html"
    context_object_name = "lesson"


class LessonCreateView(generic.CreateView):
    model = Lesson
    template_name = "lessons/create.html"
    fields = ('title', 'description', 'publish', 'prerequisite',
              'content', 'section', 'duration', 'sort_order',)


class LessonUpdateView(generic.UpdateView):
    model = Lesson
    template_name = 'lessons/edit.html'
    context_object_name = 'lesson'
    fields = fields = ('title', 'description', 'publish', 'prerequisite',
                       'content', 'section', 'duration', 'sort_order',)


class LessonDeleteView(generic.DeleteView):
    model = Lesson
    template_name = ''
