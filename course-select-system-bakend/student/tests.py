#from django.test import TestCase

# Create your tests here.

import requests, pprint, json

payload = {
    'number':'2001210111',
}
#注意post方法传递的data默认不是json的格式
#1.data参数你想要发送一些编码为表单形式的数据——非常像一个 HTML 表单。要实现这个，只需简单地传递一个字典给 data 参数。
# 你的数据字典在发出请求时会自动编码为表单形式，header默认Content-Type: application/x-www-form-urlencoded，
response = requests.post('http://localhost/api/student/listcourses', data=payload)

pprint.pprint(response.json())