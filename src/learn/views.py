from django.views import generic
from utils.models import *


class HomePage(generic.TemplateView):
    template_name           = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['featured'] = ElPath.objects.filter(featured=True)[:5]
        context['courses']  = ElPath.objects.select_related('category').all().order_by('-created_on')
        context['title']    = "Elearning Platform"
        return context


class AboutPage(generic.TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        context['title']    = "About Us"
        return context

class ContactPage(generic.TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        context['title'] = "Contact Us"
        return context

class Web(generic.TemplateView):
    template_name = "web/web.html"
