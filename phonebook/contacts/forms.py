from django import forms
from contacts.models import worker
from django.contrib.auth.forms import AuthenticationForm
class workerform(forms.ModelForm):
    class Meta:
        model=worker
        fields=("FIO","gen","work_number","mobi_number","email","struct")


class loginform(AuthenticationForm):
    username=forms.CharField(label="username")
    password=forms.CharField(label="password",widget=forms.PasswordInput)
        
