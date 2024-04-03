from django.urls import path, re_path

import user.views as user

urlpatterns = [
    path('', user.index, name='main_page'),
    path('registration/', user.registration, name='registration'),
    path('registration/check/', user.registration_check, name='registration_check'),
    path('login/', user.login, name='login'),
    path('login/check/', user.login_check, name='login_check'),
    path('login/user/<slug:name>/', user.user_page, name='user_page'),
]
