from django.http import JsonResponse
from course.models import Course
from student.models import Student

from django.core import serializers
from django.db import transaction
import json
# Create your views here.

def listcourses(request):

    #反序列化：使用vue axios的时候使用这种序列化方法
    receive_data = json.loads(request.body.decode())
    studentNumber = receive_data['number']

    #反序列化：注意这个方法是给test.py中使用post默认的数据格式不是json的时候用的，在vue axios中传递过来的参数都是json的格式，需要用上面的那种方法
    #studentNumber = request.POST.get('number')
    studentQ =Student.objects.get(number=studentNumber)
    courseAll = studentQ.courses.all()
    data = {}
    data['courses'] = json.loads(serializers.serialize("json", courseAll))

    return JsonResponse(data)

def choosecourse(request):

    # 使用vue axios的时候使用这种方法
    receive_data = json.loads(request.body.decode())
    # print(receive_data)
    studentNumber = receive_data['number']
    courseNumber = receive_data['courseNumber']

    # 注意这个方法是给test.py中使用post默认的数据格式不是json的时候用的，在vue axios中传递过来的参数都是json的格式，需要用上面的那种方法
    # studentNumber = request.POST.get('number')
    # courseNumber = request.POST.get('courseNumber')

    try:
        with transaction.atomic():
            studentQ = Student.objects.get(number=studentNumber)
            courseC = Course.objects.get(number=courseNumber)

            #检查是否选过这门课
            if courseC in studentQ.courses.all():
                return JsonResponse({'ret': '1', 'msg': '您已经选过这门课！'})

                #检查是否有课程上课时间冲突
            for course in studentQ.courses.all():
                if course.time ==  courseC.time:
                    return JsonResponse({'ret': '1', 'msg': '当前课程和您已选课程的上课时间有冲突！'})

            studentQ.courses.add(courseC)
            courseC.cur_number += 1
            courseC.save()

    except Exception as e:
        return JsonResponse({'ret':'1', 'msg':'选课未成功！'})

    return JsonResponse({'ret':'0', 'msg':'选课成功！'})


def dropcourse(request):

    # 使用vue axios的时候使用这种方法
    receive_data = json.loads(request.body.decode())
    # print(receive_data)
    studentNumber = receive_data['number']
    courseNumber = receive_data['courseNumber']

    # 注意这个方法是给test.py中使用post默认的数据格式不是json的时候用的，在vue axios中传递过来的参数都是json的格式，需要用上面的那种方法
    # studentNumber = request.POST.get('number')
    # courseNumber = request.POST.get('courseNumber')

    try:
        with transaction.atomic():
            studentQ = Student.objects.get(number=studentNumber)
            courseD = Course.objects.get(number=courseNumber)
            studentQ.courses.remove(courseD)
            courseD.cur_number -= 1
            courseD.save()

    except Exception as e:
        return JsonResponse({'ret':'1', 'msg':'退课未成功'})

    return JsonResponse({'ret':'0', 'msg':'退课成功'})


