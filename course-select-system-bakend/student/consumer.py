import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursems.settings')
django.setup()
import json, pika
from course.models import Course
from models import Student

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='work',durable=True)
print('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    #注意反序列化
    print("[x] Received %r" % json.loads(body))

    #反序列化 需要将字节流转化为相应的python格式
    data = json.loads(body)

    studentNumber = data['number']
    courseNumber = data['courseNumber']

    studentQ = Student.objects.get(number=studentNumber)
    courseC = Course.objects.get(number=courseNumber)

    studentQ.courses.add(courseC)
    courseC.cur_number += 1
    courseC.save()

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='work')
channel.start_consuming()