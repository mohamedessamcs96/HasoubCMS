from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


from .models import *

class NewUserForm(UserCreationForm):
    class Meta:
        model=AppUser
        fields=('email','username','parent_phone','birthdate','gender','is_admin','is_superuser','is_staff','password1','password2')
        #fields='__all__'


