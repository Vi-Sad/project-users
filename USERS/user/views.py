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
posts = [
    {
        'name': 'User_1',
        'title': 'Lorem',
        'description': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. '
                       'Iste in neque adipisci distinctio dolor quam!',
    },
    {
        'name': 'User_2',
        'title': 'Lorem (part 2)',
        'description': 'Continuation lorem. Lorem ipsum dolor sit amet consectetur adipisicing elit. '
                       'A hic non nam asperiores nihil adipisci ducimus!',
    }
]
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
    for i in users:
        if i['email'] == email:
            if i['email'] == email and i['password'] == password:
                active_user = i['name']
                message = 'Success'
                url = f'http://127.0.0.1:8000/login/user/{active_user}/'
            else:
                url = 'http://127.0.0.1:8000/login/'
                message = 'Invalid email or password'
            return render(request, 'login_check.html', context={'message': message, 'url': url})


def user_page(request, name):
    if any(x['name'] == name for x in users):
        return render(request, 'info_user.html', context={'name': name, 'posts': posts})
    else:
        return HttpResponseNotFound('<h1>Error 404. Page not found</h1>')


def add_post(request, name):
    title = request.GET['title']
    description = request.GET['description']
    if any(x['name'] == name for x in users):
        url = f'http://127.0.0.1:8000/login/user/{name}/'
        if title == '' or description == '':
            message = 'Error. Empty fields are not allowed'
        else:
            message = 'Success'
            posts.append({'name': name, 'title': title, 'description': description})
        return render(request, 'add_post.html', context={'url': url, 'message': message})
    else:
        return HttpResponseNotFound('<h1>Error 404. Page not found</h1>')


def info_user(request, name):
    if any(x['name'] == name for x in users):
        return render(request, 'info_user.html', context={'name': name, 'users': users, 'posts': posts})
    else:
        return HttpResponseNotFound('<h1>Error 404. Page not found</h1>')
