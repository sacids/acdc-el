from django.urls import path
from . import views

urlpatterns = [
    # announcements
    path('announcements', views.Announcements.as_view({'get': 'lists'})),
    path('announcements/retrieve/<str:table_name>/<str:table_id>',
         views.Announcements.as_view({'get': 'retrieve'})),
    path('announcements/create',
         views.Announcements.as_view({'post': 'create'})),

    # feedback
    path('feedback', views.Feedback.as_view({'get': 'lists'})),
    path('feedback/retrieve/<str:table_name>/<str:table_id>',
         views.Feedback.as_view({'get': 'retrieve'})),
    path('feedback/create',
         views.Feedback.as_view({'post': 'create'})),

    # discussions
    path('discussions', views.Discussions.as_view({'get': 'lists'})),
    path('discussions/retrieve/<str:table_name>/<str:table_id>',
         views.Discussions.as_view({'get': 'retrieve'})),
    path('discussions/create',
         views.Discussions.as_view({'post': 'create'})),

    # ratings
    path('ratings', views.Ratings.as_view({'get': 'lists'})),
    path('ratings/retrieve/<str:table_name>/<str:table_id>',
         views.Ratings.as_view({'get': 'retrieve'})),
    path('ratings/create',
         views.Ratings.as_view({'post': 'create'})),

    # notes
    path('notes', views.Notes.as_view({'get': 'lists'})),
    path('notes/retrieve/<str:table_name>/<str:table_id>',
         views.Notes.as_view({'get': 'retrieve'})),
    path('notes/create',
         views.Notes.as_view({'post': 'create'})),
]
