from django.urls import path, re_path

import user.views as user

urlpatterns = [
    path('', user.index),
]