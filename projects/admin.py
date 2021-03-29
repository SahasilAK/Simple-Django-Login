from django.contrib import admin
from projects.models import ProjectsModel

class ProjectsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
admin.site.register(ProjectsModel,ProjectsAdmin)
