from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import generic

# Create your views here.
# class CourseListView(generic.ListView):
#     model           = Course
#     template_name   = "course_list.html"
#     paginate_by     = 8

#     def get_queryset(self, *args, **kwargs):
#         if self.kwargs:
#             return Course.objects.select_related('instructor').filter(category=self.kwargs['category_id']).order_by('-created_on')
#         else:
#             return Course.objects.select_related('instructor').all().order_by('-created_on')
        
    
# class CourseDetailView(generic.DetailView):
#     model           = Course
#     template_name   = "course_detail.html"
    
#     def get_context_data(self, **kwargs):
#             course_id           = self.kwargs['pk']
#             context             = super(CourseDetailView, self).get_context_data(**kwargs)
#             context['lessons']  = Lesson.objects.filter(crs_id=course_id)
#             context['featured_courses'] = Course.objects.filter(featured=True)
#             return context

