from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *

# Create your views here.

active_user = None
display_users = User.objects.all()
posts = Post.objects.all()


def index(request):
    return render(request, 'index.html', {'users': display_users, 'posts': posts})


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def registration_check(request):
    global message
    name = request.GET['name']
    email = request.GET['email']
    password = request.GET['password']
    if all([x.name != name for x in display_users]):
        User.objects.create(name=name, email=email, password=password)
        message = 'Success'
        url = 'http://127.0.0.1:8000/'
    else:
        message = f'A user named "{name}" already exists'
        url = 'http://127.0.0.1:8000/registration/'
    return render(request, 'registration_check.html', context={'message': message, 'url': url})


def login_check(request):
    global message, active_user
    email = request.GET['email']
    password = request.GET['password']
    if any(x.email == email and x.password == password for x in display_users):
        for i in display_users:
            if i.email == email and i.password == password:
                active_user = i.name
        message = 'Success'
        url = f'http://127.0.0.1:8000/login/user/{active_user}/'
    else:
        url = 'http://127.0.0.1:8000/login/'
        message = 'Invalid email or password'
    return render(request, 'login_check.html', context={'message': message, 'url': url})


def user_page(request, name):
    if any(x.name == name for x in display_users):
        return render(request, 'info_user.html', context={'name': name, 'posts': posts})
    else:
        return HttpResponseNotFound('<h1>Error 404. Page not found</h1>')


def add_post(request, name):
    title = request.GET['title']
    description = request.GET['description']
    if any(x.name == name for x in display_users):
        url = f'http://127.0.0.1:8000/login/user/{name}/'
        if title == '' or description == '':
            message = 'Error. Empty fields are not allowed'
        else:
            message = 'Success'
            Post.objects.create(name=name, title=title, description=description)
        return render(request, 'add_post.html', context={'url': url, 'message': message})
    else:
        return HttpResponseNotFound('<h1>Error 404. Page not found</h1>')


def info_user(request, name):
    if any(x.name == name for x in display_users):
        return render(request, 'info_user.html', context={'name': name, 'users': display_users, 'posts': posts})
    else:
        return HttpResponseNotFound('<h1>Error 404. Page not found</h1>')
