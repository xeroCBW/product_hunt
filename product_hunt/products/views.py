from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.


def products_list(request):

    return render(request,'products_list.html')
    pass

@login_required
def publish(request):

    if request.method == 'GET':
        return render(request,'products_publish.html')

    elif request.method == 'POST':

        app_name = request.POST['app_name']
        introduction = request.POST['introduction']
        link = request.POST['link']
        try:
            icon = request.FILES['icon']
            image = request.FILES['pic']
        except Exception as err:
            return render(request,'products_publish.html',{'msg':'请上传图片'})

        product = Product()
        product.app_name = app_name
        product.introduction = introduction
        product.link = link
        product.icon = icon
        product.image = image
        product.hunter = request.user
        product.pub_date = timezone.datetime.now()
        product.save()

        return redirect('主页')
