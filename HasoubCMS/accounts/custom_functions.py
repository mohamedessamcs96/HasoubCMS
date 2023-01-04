from .models import AppUser
#from ..models

def get_error_message(request):
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']
    email=request.POST['email']
    username=request.POST['username']
    if AppUser.objects.filter(username=username).exists():
        return "Username already exists"
    if password!=confirm_password:
        return "The Passwords didn't match"
    if AppUser.objects.filter(email=email).exists():
        return "Email already exists"