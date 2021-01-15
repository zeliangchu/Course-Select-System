from django.db import models
from django.utils.html import format_html

# Create your models here.


class Course(models.Model):
    number = models.IntegerField(verbose_name="课程编号")
    name = models.CharField(max_length=50, verbose_name="课程名")
    credit = models.IntegerField(verbose_name="学分")
    max_number = models.IntegerField(verbose_name="课程最大人数")
    cur_number = models.IntegerField(verbose_name="课程当前人数")
    teacher = models.CharField(max_length=50, verbose_name="任课教师")
    time = models.CharField(max_length=50, verbose_name="上课时间")
    location = models.CharField(max_length=50, verbose_name="上课地点")
    introduction = models.CharField(max_length=200, verbose_name="课程介绍")

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '所有课程'

    def __str__(self):
        return self.name

    #自定义方法 主要负责给课程标注颜色
    def Status(self):
        if self.max_number - self.cur_number > 10:
            format_td = format_html('<span style="padding:2px;background-color:green;color:white">充足</span>')
        if 0 < self.max_number - self.cur_number <= 10:
            format_td = format_html('<span style="padding:2px;background-color:yellow;color:black">紧张</span>')
        if self.cur_number == self.max_number:
            format_td = format_html('<span style="padding=2px;background-color:red;color:white">已满</span>')
        return format_td
    Status.short_description = '当前容量'