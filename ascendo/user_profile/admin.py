from django.contrib import admin

from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['name', 'college', 'nick_name']
    list_display = ['name', 'college']
    list_filter = ['language', 'code', 'has_completed']
