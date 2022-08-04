from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("signup/", views.signup, name='register'),
    path("login/", views.login, name='login')
]