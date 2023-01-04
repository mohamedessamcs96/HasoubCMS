from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.





class AppUser(AbstractUser):
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female')
    )
    email=models.EmailField(max_length=50,unique=True)
    #USERNAME_FIELD='email'
    #REQUIRED_FIELDS=['email']
    parent_phone=models.CharField(max_length=18,default='+20')
    birthdate=models.DateField(null=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES, default='male')
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)



    

