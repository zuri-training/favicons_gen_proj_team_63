from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_page, name='home'),
    path("signup/", views.signup, name='register'),
    path("login/", views.login, name='login'),
    path('upload/', views.upload,name='upload'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)