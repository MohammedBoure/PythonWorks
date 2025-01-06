from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):  
    return render(request, 'pages/index.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "Pluto" and password == "K3cZE4tu":
            return render(request, 'pages/admin.html', {'name': username})
        else:
            error_message = "اسم المستخدم أو كلمة المرور غير صحيحة!"
            return render(request, 'pages/login.html', {'error': error_message})

    return render(request, 'pages/login.html')
 

def admin(request):
    return render(request, 'pages/admin.html')

def product_management(request):
    return render(request, 'pages/product_management.html')

def upload_product(request):
    if request.method == 'POST':
        return HttpResponse("تم رفع المنتج بنجاح")
    return redirect('pages/product_management')

