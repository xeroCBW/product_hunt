from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register,name='注册页面'),
    path('login/', views.login,name='登录页面'),

]
