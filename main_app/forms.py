from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['city', 'img']

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name']