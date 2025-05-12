from django.db import models
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class worker(models.Model):
    user=models.OneToOneField("User", verbose_name='Пользователь',on_delete=models.CASCADE,null=True,blank=True)
    FIO=models.CharField("ФИО",max_length=45)
    gen=models.ForeignKey("pol", verbose_name='Пол', on_delete=models.CASCADE,null=True,blank=True)
    work_number=models.CharField('рабочий номер', max_length=9)
    mobi_number=models.CharField('мобильный номер',max_length=9)
    email=models.EmailField("email",max_length=45)
    struct=models.ForeignKey("structure", verbose_name='Подразделение', on_delete=models.CASCADE,null=True,blank=True)


 

class pol(models.Model):
    polcnom=models.CharField(max_length=3)

    def __str__(self):
        return self.polcnom
    
class structure(models.Model):
    structcnom=models.CharField()
    def __str__(self):
        return self.structcnom


    

    


    


    
