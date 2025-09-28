from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),              # /users/
    path("login/", views.login_view, name="login"),   # /users/login/
    path("logout/", views.logout_view, name="logout"),# /users/logout/
]
