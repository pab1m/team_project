from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    return render(request,  'index.html')
    # return HttpResponse('Hello world!@ test')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        users = User.objects.all()
        print(f"{users} -------------------------------")

        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('museum:index')

    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return redirect('museum:index')
