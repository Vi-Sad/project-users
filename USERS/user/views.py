from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

users = [{
    'name': 'Victoria',
    'email': 'sadovskaya.vicka@yandex.ru',
    'password': 'pass-victoria-2024',
}, {'name': 'Kseniya',
    'email': 'k.sadovskaya2022@gmail.com@yandex.ru',
    'password': 'pass-kseniya-2024', }]


def index(request):
    return render(request, 'index.html')


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
        message = f'Success {users}'
    else:
        message = f'A user named "{name}" already exists'
    return render(request, 'registration_check.html', context={'message': message})
