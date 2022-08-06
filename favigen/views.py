from multiprocessing import context
from django.views.generic import TemplateView
from unicodedata import name
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home_page(request):
    return render(request, "favigen/base.html")


def signup(request):
    return render(request, "favigen/sign-up.html")


def login(request):
    return render(request, "favigen/login.html")

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context["url"] = fs.url(name)
    return render(request, 'favigen/upload.html', context)
    