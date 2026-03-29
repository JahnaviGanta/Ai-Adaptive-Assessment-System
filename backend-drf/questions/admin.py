from django.contrib import admin
from . models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display=['id','assignment','question','answer','difficulty']
    list_filter =['assignment']
    search_fields=['assignment__title','difficulty']
    ordering=['id']


admin.site.register(Question, QuestionAdmin)
