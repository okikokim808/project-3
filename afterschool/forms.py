from django import forms
from .models import Parent, DailyInfo, Student
from django.contrib.auth.models import User

# these 3 things work together: froms.py UserForm class, views.py register() function, and registration.html
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
