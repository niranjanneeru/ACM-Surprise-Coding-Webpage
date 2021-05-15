from django.contrib import admin

from .models import Question, Response, Challenge

admin.site.register(Response)


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    search_fields = ['question', 'answer']
    list_display = ['question', 'answer']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question', 'answer']
    list_display = ['question', 'is_active', 'answer']
