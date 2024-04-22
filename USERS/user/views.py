from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *
from .forms import *
from datetime import datetime

# Create your views here.

active_user = None
display_users = User.objects.all()
posts = Post.objects.all()
personal = PersonalInformation.objects.all()


def index(request):
    return render(request, 'index.html', {'users': display_users.all(), 'posts': posts.all()})


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def registration_check(request):
    global message
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST['password']
    if len(name) == 0 or len(email) == 0 or len(password) == 0:
        message = 'Error. Empty fields are not allowed'
        url = 'http://127.0.0.1:8000/registration/'
    elif all([x.name != name for x in display_users]):
        User.objects.create(name=name, email=email, password=password)
        PersonalInformation.objects.create(name=name, status='no status')
        message = 'Success! Restart the page for the changes to take effect'
        url = 'http://127.0.0.1:8000/'
    else:
        message = f'A user named "{name}" already exists'
        url = 'http://127.0.0.1:8000/registration/'
    return render(request, 'registration_check.html', context={'message': message, 'url': url})


def login_check(request):
    global message, active_user
    email = request.POST.get('email')
    password = request.POST.get('password')
    if len(email) == 0 or len(password) == 0:
        message = 'Error. Empty fields are not allowed'
        url = 'http://127.0.0.1:8000/login/'
    elif any(x.email == email and x.password == password for x in display_users):
        for i in display_users:
            if i.email == email and i.password == password:
                active_user = i.name
        message = 'Success! Restart the page for the changes to take effect'
        url = f'http://127.0.0.1:8000/login/user/{active_user}/'
    else:
        message = f'Invalid email or password'
        url = 'http://127.0.0.1:8000/login/'
    return render(request, 'login_check.html', context={'message': message, 'url': url})


def user_page(request, name):
    if any(x.name == name for x in display_users):
        return render(request, 'info_user.html', context={'name': name, 'posts': posts.all(),
                                                          'personal_information': AddPersonalInformation(),
                                                          'personal': personal})
    else:
        return HttpResponseNotFound('<style>body {background-color: black; color: white;}</style>'
                                    '<h1>Error 404. Page not found</h1>')


def add_post(request, name):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if any(x.name == name for x in display_users):
        url = f'http://127.0.0.1:8000/login/user/{name}/'
        if title == '' or description == '':
            message = 'Error. Empty fields are not allowed'
        else:
            message = 'Success! Restart the page for the changes to take effect'
            Post.objects.create(name=name, title=title, description=description)
            Post.objects.filter(title=title).update(date_publication=datetime.now(), date_change=datetime.now())
        return render(request, 'add_post.html', context={'url': url, 'message': message})
    else:
        return HttpResponseNotFound('<style>body {background-color: black; color: white;}</style>'
                                    '<h1>Error 404. Page not found</h1>')


def edit_post(request, post_id):
    global active_user
    for i in posts.all():
        if i.id == post_id:
            active_user = i.name
    return render(request, 'edit_post.html', context={'posts': posts.all(), 'post_id': post_id, 'name': active_user})


def edit_post_check(request, post_id):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if len(title) == 0 or len(description) == 0:
        message = 'Error. Empty fields are not allowed'
    else:
        Post.objects.filter(id=post_id).update(title=title, description=description, date_change=datetime.now())
        message = 'Success! Restart the page for the changes to take effect'
    return render(request, 'edit_post_check.html', context={'name': active_user, 'message': message})


def delete_post(request, post_id):
    global active_user
    for i in posts:
        if i.id == post_id:
            active_user = i.name
    Post.objects.filter(id=post_id).delete()
    return render(request, 'delete_post.html', context={'name': active_user})


def info_user(request, name):
    if any(x.name == name for x in display_users):
        return render(request, 'info_user.html',
                      context={'name': name, 'users': display_users.all(), 'posts': posts.all(),
                               'personal_information': AddPersonalInformation(), 'personal': personal})
    else:
        return HttpResponseNotFound('<style>body {background-color: black; color: white;}</style>'
                                    '<h1>Error 404. Page not found</h1>')


def edit_status(request, name):
    global status_current
    if request.method == 'POST':
        status = request.POST.get('status')
        form = AddPersonalInformation(request.POST)
        if form.is_valid():
            PersonalInformation.objects.filter(name=name).update(status=status)
            message = f'Success! The status will be updated after the server is restarted'
        else:
            message = f'Error: {form.errors}'
    else:
        for i in personal:
            if i.name == name:
                status_current = i.status
        message = f'Your current status: {status_current}'
    return render(request, 'edit_status.html', context={'name': name, 'message': message})


def edit_birthday(request, name):
    birthday = request.POST.get('birthday')
    PersonalInformation.objects.filter(name=name).update(birthday=birthday)
    message = 'Success! Birthday'
    return render(request, 'edit_birthday.html', context={'name': name, 'message': message})
