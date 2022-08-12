from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

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


class CustomAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  CustomUser
        fields =  ('email', 'password')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            'class':'form-inpu',
            'id': 'email',
            'type': 'email',
            'placeholder': 'Email'
        })
        self.fields["password"].widget.attrs.update({
            'class':'form-input',
            'id': 'password',
            'type': 'password',
            'placeholder': 'Password'
        })

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')



# class AccountUpdateform(forms.ModelForm):
#     """
#       Updating User Info
#     """
#     class Meta:
#         model  = CustomUser
#         fields = ('email', 'username')
#         widgets = {
#                    'email':forms.TextInput(attrs={'class':'form-control'}),
#                    'password':forms.TextInput(attrs={'class':'form-control'}),
#         }

#     def __init__(self, *args, **kwargs):
#         """
#           specifying styles to fields 
#         """
#         super(AccountUpdateform, self).__init__(*args, **kwargs)
#         for field in (self.fields['email'],self.fields['username']):
#             field.widget.attrs.update({'class': 'form-control '})

#     def clean_email(self):
#         if self.is_valid():
#             email = self.cleaned_data['email']
#             try:
#                 account = CustomUser.objects.exclude(pk = self.instance.pk).get(email=email)
#             except CustomUser.DoesNotExist:
#                 return email
#             raise forms.ValidationError("Email '%s' already in use." %email)
#     def clean_username(self):
#         if self.is_valid():
#             username = self.cleaned_data['username']
#             try:
#                 account = CustomUser.objects.exclude(pk = self.instance.pk).get(username=username)
#             except CustomUser.DoesNotExist:
#                 return username
#             raise forms.ValidationError("Username '%s' already in use." % username)