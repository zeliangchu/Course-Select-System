from django.contrib import admin
from  .models import Student, StudentCourses
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'department', 'major']
    search_fields = ['name', 'number', 'department', 'major']
    list_filter = ['major']
    list_per_page = 10
    ordering = ['number']
    view_on_site = False



admin.site.register(Student, StudentAdmin)


#class StudentCoursesAdmin(admin.ModelAdmin):

#admin.site.register(StudentCourses)

admin.site.site_title = '选课管理系统'
admin.site.site_header = '选课管理系统'