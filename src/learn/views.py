from django.views import generic
from utils.models import *


class HomePage(generic.TemplateView):
    template_name           = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['featured'] = ElPath.objects.filter(featured=True)[:5]
        context['courses']  = ElPath.objects.select_related('category').all().order_by('-created_on')
        return context


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class Web(generic.TemplateView):
    template_name = "web/web.html"
