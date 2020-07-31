from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
import profiles.urls
import accounts.urls, course.urls, utils.urls
from . import views

# Personalized admin site settings like title and header
admin.site.site_title = "Learn Site Admin"
admin.site.site_header = "Learn Administration"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("users/", include(profiles.urls)),
    path("admin/", admin.site.urls),
    path("", include(accounts.urls)),
    path("web/", views.Web.as_view(), name="Web"),
    #path("course/", include(course.urls)),

    #api
    path('api/', include('api.urls'))
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
