from django.contrib import admin

from experience.models import Experience,Responsibility

class ExperInline(admin.TabularInline):
    model=Responsibility
    extra=1
class ResponsibilityAdmin(admin.ModelAdmin):
    inlines=[ExperInline]
admin.site.register(Experience,ResponsibilityAdmin)
admin.site.register(Responsibility)