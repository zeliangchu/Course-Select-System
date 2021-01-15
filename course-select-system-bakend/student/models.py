from django.db import models
from course.models import Course
# Create your models here.


class Student(models.Model):
    number = models.CharField(max_length=50, verbose_name="学号")
    name = models.CharField(max_length=50, verbose_name="姓名")
    gender = models.CharField(max_length=10, verbose_name="性别")
    department = models.CharField(max_length=50, verbose_name="院系")
    major = models.CharField(max_length=50, verbose_name="专业")
    courses = models.ManyToManyField(Course, through='StudentCourses')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '所有学生'

    def __str__(self):
        return self.name

class StudentCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)