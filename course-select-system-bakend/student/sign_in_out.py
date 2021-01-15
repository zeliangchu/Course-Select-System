from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
import json

#登录处理
def signin(request):
    #前端如果传过来的是json格式的数据就需要使用下面的方式
    receive_data = json.loads(request.body.decode())
    studentNumber = receive_data['number']
    passWord = receive_data['password']

    #如果前端传过来的是x-www-form-urlencoded格式的数据就需要使用下面的方式
    #从HTTP POST请求中获取学号、密码参数
    #studentNumber = request.POST.get('number')
    #passWord = request.POST.get('password')

    #使用django auth库中的方法校验用户名和密码
    user = authenticate(username=studentNumber, password=passWord)

    #如果能够找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            login(request, user)
            #把用户的学号存到session里面 ！！！！
            request.session['number'] = 'studentNumber'

            return JsonResponse({'ret':0})
        else:
            return JsonResponse({'ret':1, 'msg':'用户已经被禁用'})
    else:
        return JsonResponse({'ret':1, 'msg':'用户名或者密码错误'})

#登出处理
def signout(request):
    logout(request)
    return JsonResponse({'ret':0})
