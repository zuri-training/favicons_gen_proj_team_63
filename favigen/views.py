from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render, redirect
from favigen.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def home_page(request):
    return render(request, "favigen/home.html")


def signup_page(request):
    """
    This view renders the signup page and then takes in user data 
    (First Name, Email and Password) from the HTML form as a POST request.
    It then extracts the user's first name from the form and uses it in a 
    custom message if the registration is successful, after which it 
    redirects the user to the home page.
    """
    # if not request.user.is_anonymous:
    #     return redirect("favigen:home")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            f_name = form.cleaned_data.get("first_name")
            messages.success(request, f"Registration successful for {f_name}")
            return redirect("favigen:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = CustomUserCreationForm()
    return render(
        request=request,
        template_name="favigen/sign-up.html",
        context={"signup_form": form},
    )


def login_page(request):
    user = request.user
    # if user.is_authenticated:
    #     return redirect("favigen:home")

    if request.POST:
        form = CustomAuthenticationForm(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")

        if user := authenticate(email=email, password=password):
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("favigen:home")
        else:
            messages.error(request, "Please enter correct details")
    else:
        form = CustomAuthenticationForm()

    context = {"login_form": form}
    return render(request, "favigen/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("favigen:home")


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context["url"] = fs.url(name)
    return render(request, "favigen/upload.html", context)
