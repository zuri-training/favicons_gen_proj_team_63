from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'input type':'text',
            'id': 'firstName',
            'name': 'first_name',
            'placeholder': 'First Name'
        })
        self.fields["email"].widget.attrs.update({
            'input type':'email',
            'id': 'email',
            'name': 'email',
            'placeholder': 'Email Address'
        })
        self.fields["password1"].widget.attrs.update({
            'type':'password',
            'id': 'password',
            'name': 'password',
            'placeholder': 'Password'
        })
        self.fields["password2"].widget.attrs.update({
            'type':'password',
            'id': 'password',
            'name': 'password',
            'placeholder': 'Password again'
        })


    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')