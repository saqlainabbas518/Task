from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterationForm(UserCreationForm):
      email = forms.EmailField()

      class meta:
           model =User
           fields = ['username' , 'email' , 'password1' , 'password2']

      class UserUpdateForm(forms.ModelForm):
          email = User
          fields = ['username','email']

      class ProfileUpdateForm(forms.ModelForm):
          class Meta:
              model = Profile
              fields = ['image']

