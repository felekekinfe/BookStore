from django import forms
from .models import Account
class RegistrationForm(forms.ModelForm):

    class Meta:
        model=Account
        fields=['username','first_name','last_name','email','phone','password']
class LoginForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['email','password']
