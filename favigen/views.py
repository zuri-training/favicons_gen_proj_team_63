from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "favigen/base.html")


def signup(request):
    return render(request, "favigen/sign-up.html")


def login(request):
    return render(request, "favigen/login.html")