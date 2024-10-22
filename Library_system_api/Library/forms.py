from .models import Book, User
from django.forms import ModelForm
from django.contrib.auth.forms import  AuthenticationForm
from django import forms
from django.forms.widgets import TextInput, PasswordInput

class CreateuserForm(ModelForm):

    class Meta:
        model = User
        fields = [
            "username",
            "Email",
            "password",
            "confirm_password",
        ]

class loginForm(AuthenticationForm):

    
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)

class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = "__all__"