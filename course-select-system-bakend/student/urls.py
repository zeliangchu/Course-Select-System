from django.urls import path

from student import sign_in_out, views
from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [
    path('listcourses', views.listcourses),
    path('choosecourse', views.choosecourse),
    path('dropcourse', views.dropcourse),
    path('signin', obtain_jwt_token),
    #path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
]