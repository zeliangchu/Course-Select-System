import json, pika
from django.http import JsonResponse
from student.models import Student
from course.models import Course
from django.db import transaction

def choosecourse(request):

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='work', durable=True)


    # 使用vue axios的时候使用这种方法
    receive_data = json.loads(request.body.decode())
    # print(receive_data)
    studentNumber = receive_data['number']
    courseNumber = receive_data['courseNumber']

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

    except Exception as e:
        return JsonResponse({'ret':'1', 'msg':'选课未成功！'})

    #reveived_data需要进行序列化之后转化为字节流在放到body中

    channel.basic_publish(exchange='',
                          routing_key='work',
                          body=receive_data,
                          properties=pika.BasicProperties(
                              delivery_mode=2,#make message persistent
                          ))

    print("send data for consumer")

    connection.close()

    return JsonResponse({'ret':'0', 'msg':'已经将您的选课信息发布到队列中，请到查看课程界面查看选课结果！'})