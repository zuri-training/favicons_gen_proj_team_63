from django.shortcuts import render, redirect
from favigen.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def home_page(request):
    return render(request, "favigen/home.html")


# def signup(request):
#     return render(request, "favigen/sign-up.html")


def login(request):
    return render(request, "favigen/login.html")



def signup(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("favigen:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CustomUserCreationForm()
	return render (request=request, template_name="favigen/sign-up.html", context={"signup_form":form})

    # if request.method == 'POST':
    #     first_name = request.POST['first_name'],
    #     # last_name = request.POST['last_name'],
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     newuser= CustomUser.objects.create_user(first_name=first_name, email=email, password=password)
    #     newuser.save()
    #     print('user created')
    #     return redirect('/home')
    # else:
    #     return render(request,'register.html')