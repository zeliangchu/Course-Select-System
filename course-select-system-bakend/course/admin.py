from django.contrib import admin
from  .models import Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'credit', 'max_number', 'cur_number', 'teacher', 'time', 'location', 'Status']
    list_filter = ['credit', 'time', 'location', 'cur_number', 'teacher']
    search_fields = ['name','teacher']
    list_per_page = 10
    ordering = ['number']
    view_on_site = False


admin.site.register(Course, CourseAdmin)

admin.site.site_title = '选课管理系统'
admin.site.site_header = '选课管理系统'