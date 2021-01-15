from django.http import JsonResponse
from course.models import Course
from django.core import serializers
import json
# Create your views here.

def listcourses(request):
    courseAll = Course.objects.all()
    data = {}
    #序列化
    data['courses'] = json.loads(serializers.serialize("json", courseAll))
    return JsonResponse(data)