from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


from .models import *

class NewUserForm(UserCreationForm):
    class Meta:
        model=AppUser
        fields=('email','username','parent_phone','birthdate','gender','is_admin','is_superuser','is_staff','password1','password2')
        #fields='__all__'



class AddClass(UserCreationForm):
    class Meta:
        model=Class
        fields=['classcode','name','coursesid','datefrom','dateto','studentname','teachername']
        #fields='__all__'



class AddCourse(UserCreationForm):
    class Meta:
        model=Course
        #coursecode = models.CharField(max_length=50)
        #name = models.CharField(max_length=50)
        #shortname = models.CharField(max_length=50, default='X')
        fields=('coursecode','name','shortname')
        #fields='__all__'

