from django.urls import path
from . import views

app_name = "favigen"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("signup/", views.signup_page, name="signup"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("contact/", views.contact_page, name="contact"),
    path("message-sent/", views.message_sent, name="sent"),
    path("saved-icons/", views.saved_icons, name="saved"),
    path("generated-icon/<str:pk>", views.generated_icon, name="generated"),
    path("generate-icon/", views.generate_icon, name="generate"),
]
