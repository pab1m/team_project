from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request,  'index.html')
    # return HttpResponse('Hello world!@ test')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Цей логін вже зайнятий!')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=email, password=password, username=username)
                user.save()
                return redirect('/')
    else:
        return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return redirect('museum:index')


def login(request):
    return render(request,  'login.html')


def password_forgotten(request):
    return render(request,  'passwordforgotten.html')



