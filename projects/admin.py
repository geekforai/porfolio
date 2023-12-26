from django.contrib import admin
from projects.models import Projects
@admin.register(Projects)
class RegProjects(admin.ModelAdmin):
    pass
