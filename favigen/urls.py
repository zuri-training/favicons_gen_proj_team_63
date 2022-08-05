from django.urls import path
from . import views

app_name = "favigen"

urlpatterns = [
    path("", views.home_page, name='home'),
    path("signup/", views.signup, name='signup'),
    path("login/", views.login, name='login')
]