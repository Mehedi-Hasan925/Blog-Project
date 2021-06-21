from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from login_app import models

class signup_form(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.EmailField(required=True)
    last_name = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password1','password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password')


class change_profile_pic(forms.ModelForm):
    
    class Meta:
        model = models.UserProfile
        fields=('profile_pic',)
