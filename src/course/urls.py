from django.urls import path
from django.conf.urls import url

from . import views


app_name = "course"
urlpatterns = [
    path("", views.PathListView.as_view(), name="course_list"),
    path('<int:pk>-<slug:slug>', views.PathDetailView.as_view(), name='course_detail'),
    path('<int:pk>-<slug:slug>/<int:lesson_id>', views.PathDetailView.as_view(), name='cl_detail'),

    #sections
    path('section/', views.SectionListView.as_view(),name='section_list'),
    path('section/create', views.SectionCreateView.as_view(), name='section_create'),
    path('section/<int:pk>', views.SectionDetailView, name='section_detail'),
    path('section/<int:pk>/update', views.SectionUpdateView.as_view(),name='section_update'),
    path('section/<int:pk>/delete', views.SectionDeleteView.as_view(),name='section_delete'),

    #lessons
    path('lesson/', views.LessonListView.as_view(), name='lesson_list'),
    path('lesson/create', views.LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>', views.LessonDetailView, name='lesson_detail'),
    path('lesson/<int:pk>/update',views.LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete',views.LessonDeleteView.as_view(), name='lesson_delete'),
]
