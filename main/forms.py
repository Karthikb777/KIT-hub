from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note, ModRequests

class NoteForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={'accept': 'application/pdf'}))
    class Meta:
        model = Note
        fields = ( 'name', 'description', 'file', 'coverImage', 'label' )


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ( "username", "email", "password1", "password2" )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput())

class ModRequestForm(forms.ModelForm):
    class Meta:
        model = ModRequests
        fields = ( 'description', )



        