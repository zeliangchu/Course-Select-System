# Generated by Django 3.1.5 on 2021-01-07 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20210107_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '教师', 'verbose_name_plural': '所有教师'},
        ),
    ]