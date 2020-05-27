from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def register(request):


    if request.method=='GET':
        return render(request, 'register.html')
    elif request.method =='POST':
        user_name = request.POST['username']
        password = request.POST['password']

        try:
            User.objects.get(username=user_name)
            return render(request,'login.html')
        except User.DoesNotExist:
            User.objects.create_user(username=user_name,password=password)
            return redirect('主页')


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        user_nmae = request.POST['username']
        pass_word = request.POST['password']
        user = auth.authenticate(username=user_nmae,password=pass_word)
        if user is None:
            return render(request,'login.html',{'msg':'用户名或者密码错误'})
        else:
            # 回到主页
            auth.login(request,user)
            return redirect('主页')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('主页')
