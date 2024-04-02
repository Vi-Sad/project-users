from django.urls import path, re_path

import user.views as user

urlpatterns = [
    path('', user.index),
    path('registration/', user.registration, name='registration'),
    path('registration/check', user.registration_check, name='registration_check'),
    path('login/', user.login, name='login'),
]
