from django.shortcuts import render, redirect
from favigen.forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home_page(request):
    return render(request, "favigen/home.html")


# def signup(request):
#     return render(request, "favigen/sign-up.html")


# def login(request):
#     return render(request, "favigen/login.html")



def signup_page(request):
    # if not request.user.is_anonymous:
    #     return redirect("favigen:home")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            f_name = form.cleaned_data.get('first_name')
            messages.success(request, f"Registration successful for {f_name}")
            return redirect("favigen:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = CustomUserCreationForm()
    return render (request=request, template_name="favigen/sign-up.html", context={"signup_form": form})


def login_page(request):
    # if request.method == "POST":
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')

    #     user = authenticate(request=request, email=email, password=password)

    #     if user is not None:
    #         login(request, user)
    #         # f_name = form.cleaned_data.get('first_name')
    #         messages.success(request, "Welcome!")
    #         return redirect("favigen:home")
    #     messages.error(request, "Login failed, incorrect credentials")

    # context = {}
    # return render (request=request, template_name="favigen/login.html", context=context)


	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {email}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})



    # return render (request=request, template_name="favigen/sign-up.html", context={"signup_form": form})

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