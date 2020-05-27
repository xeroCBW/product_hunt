from django.shortcuts import render

# Create your views here.


def products_list(request):

    return render(request,'products_list.html')
    pass

def publish(request):

    return render(request,'products_publish.html')
    pass
