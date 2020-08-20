from django.contrib import admin
from django.apps import apps
from .models import *

# Register your models here.

class PathSectionInline(admin.StackedInline):
    model               = Section

class PathAdmin(admin.ModelAdmin):
    list_display        = ['title', 'category','featured', 'created_by','created_on']
    list_filter         = ['featured', 'created_on', 'created_by', 'category']
    list_editable       = ['featured', 'category']
    inlines             = [PathSectionInline]

admin.site.register(ElPath, PathAdmin)



class SectionLessonInline(admin.StackedInline):
    model               = Lesson

class SectionAdmin(admin.ModelAdmin):
    list_display        = ['sort_order','title', 'el_path','publish', 'created_by','created_on']
    list_filter         = ['publish', 'el_path', 'created_by']
    list_display_links  = ['title']
    list_editable       = ['publish','sort_order']
    inlines             = [SectionLessonInline]

admin.site.register(Section, SectionAdmin)











# Register your models here.


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()
for model in models:
    #print(model.name)
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass


        