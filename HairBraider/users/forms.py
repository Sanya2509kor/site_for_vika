from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "phone_number",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    phone_number = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "username",
            "email",
        )
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()