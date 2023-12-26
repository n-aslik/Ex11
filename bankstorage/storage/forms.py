from django import forms
from storage.models import  Userlogin ,Incoming,Storage,Outcoming,Branch,Branch_access
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.utils import timezone




class userform(AuthenticationForm):
    pass

class userpageform(forms.ModelForm):
    class Meta:
        model=Userlogin
        fields=['Fio','pos','Tel','rol']
        
        
class incomingform(forms.ModelForm):
    class Meta:        
        model=Incoming
        fields=['user','iname','Counti','Recipient','incoming_date','store']
        

class outcomingform(forms.ModelForm):
    class Meta:        
        model=Outcoming
        fields=['user','inc','Counto','Recipient','outcoming_date','store']
        
class storeform(forms.ModelForm):
    branch=forms.ModelChoiceField(queryset=Branch.objects.all(),label="Филиал")
    class Meta:
        model=Storage
        fields=['sname','branch']

    
       
        
        
class branchform(forms.ModelForm):
    class Meta:        
        model=Branch
        fields=['Address','bname']
        
        
class branch_accessform(forms.ModelForm):
    branch=forms.ModelChoiceField(queryset=Branch.objects.all(),label="Филиал")
    class Meta:        
        model=Branch_access
        fields=['user','branch','store']
        

class report_searchform(forms.Form):
    query_b=forms.CharField(label="Филиал", max_length=100)
    query_ds=forms.DateField(label="Начальная_Дата")
    query_de=forms.DateField(label="Конечная_Дата")

    

class loginform(userform):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
        
        
    
        
