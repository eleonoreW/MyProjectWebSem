from django import forms
from django.contrib.auth.models import User

from accounts.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'height', 'weight', 'city', 'birthday','diet']
