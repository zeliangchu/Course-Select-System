from django.db import models

# Create your models here.

class Teacher(models.Model):
    number = models.CharField(max_length=50, verbose_name="教工号")
    name = models.CharField(max_length=50, verbose_name="姓名")
    gender = models.CharField(max_length=10, verbose_name="性别")
    department = models.CharField(max_length=50, verbose_name="院系")

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '所有教师'

    def __str__(self):
        return self.name