from django.urls import path
from . import views

app_name = "favigen"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("signup/", views.signup_page, name="signup"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("upload/", views.image_upload, name="upload"),
    path("contact/", views.contact_page, name="contact"),
    path("saved-icons/", views.saved_icons, name="saved"),
    path("generated-icon/", views.generated_icon, name="generated"),
]
