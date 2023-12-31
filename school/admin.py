from django.contrib import admin
from .models import School, Department, Student


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('user', 'school_name','created_at')
    list_display_links = ('user', 'school_name')



admin.site.register(School, SchoolAdmin)
admin.site.register(Department)
admin.site.register(Student)