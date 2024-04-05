from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

users = [
    {
        'name': 'User_1',
        'email': 'user_1@email.ru',
        'password': 'pass_1',
    },
    {
        'name': 'User_2',
        'email': 'user_2@email.ru',
        'password': 'pass_2',
    },
]
posts = []
active_user = None


def index(request):
    return render(request, 'index.html', {'users': users, 'posts': posts})


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def registration_check(request):
    global message
    name = request.GET['name']
    email = request.GET['email']
    password = request.GET['password']
    if all([x['name'] != name for x in users]):
        users.append({'name': name, 'email': email, 'password': password})
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
    if any([x['email'] == email for x in users] and [x['password'] == password for x in users]):
        for i in users:
            if email == i['email']:
                active_user = i['name']
        message = 'Success'
        url = f'http://127.0.0.1:8000/login/user/{active_user}/'
    else:
        url = 'http://127.0.0.1:8000/login/'
        message = 'Invalid email or password'
    return render(request, 'login_check.html', context={'message': message, 'url': url})


def user_page(request, name):
    if any(x['name'] == name for x in users):
        return render(request, 'page_user.html', context={'name': name, 'posts': posts})
    else:
        return HttpResponseNotFound('<h1>Error 404. Page not found</h1>')


def add_post(request, name):
    title = request.GET['title']
    description = request.GET['description']
    if any(x['name'] == name for x in users):
        url = f'http://127.0.0.1:8000/login/user/{name}/'
        posts.append({'name': name, 'title': title, 'description': description})
        return render(request, 'add_post.html', context={'url': url})
    else:
        return HttpResponseNotFound('<h1>Error 404. Page not found</h1>')
