from django.contrib import admin
from . models import Assignment, AssessmentSession

class AssignmentAdmin(admin.ModelAdmin):
    list_display=['id','topic','title']
    ordering=['id']




admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(AssessmentSession)