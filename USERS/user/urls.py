from django.urls import path, re_path

import user.views as user

urlpatterns = [
    path('', user.index, name='main_page'),
    path('registration/', user.registration, name='registration'),
    path('registration/check/', user.registration_check, name='registration_check'),
    path('login/', user.login, name='login'),
    path('login/check/', user.login_check, name='login_check'),
    path('login/user/<slug:name>/', user.info_user, name='user_page'),
    path('login/post/add/', user.add_post, name='add_post'),
    path('login/post/edit/<int:post_id>/', user.edit_post, name='edit_post'),
    path('login/post/edit/<int:post_id>/check/', user.edit_post_check, name='edit_post_check'),
]
