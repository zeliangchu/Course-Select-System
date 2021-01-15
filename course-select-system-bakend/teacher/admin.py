from django.contrib import admin
from  .models import Teacher
# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'department']
    search_fields = ['name', 'number', 'department']
    list_filter = ['department']
    list_per_page = 10
    ordering = ['number']
    view_on_site = False

admin.site.register(Teacher, TeacherAdmin)

admin.site.site_title = '选课管理系统'
admin.site.site_header = '选课管理系统'