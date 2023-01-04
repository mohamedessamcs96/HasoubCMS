# Some coding notes

### for Custom User Data base model i have to do the foloing 
    *. python manage.py migrate --run-syncdb
    *. AUTH_USER_MODEL='accounts.AppUser'
    *. class AppUser(AbstractUser):
    *. when i get error in create superuser put the field null=true or set default value...




### Static files

*. STATIC_URL = '/static/'
*. STATIC_ROOT=os.path.join(BASE_DIR,'static/')
*. STATICFILES_DIR=[os.path.join(BASE_DIR,'static')]
python manage.py collect static
*. import os
*. MEDIA_URL='/media/'
*. MEDIA_ROOT=os.path.join(BASE_DIR,'meida/')

### Messages
*. Settings.py 
import os
from django.contrib.messages import constants as messages

MESSAGE_TAGS={
    messages.DEBUG:'alert-secondary',
    messages.INFO:'alert-info',
    messages.SUCCESS:'alert-success',
    messages.WARNING:'alert-warning',
    messages.ERROR:'alert-danger',

}

.* Messages.html
    {% for message in messages %}
        <div class="container-fluid p-0">
        <div class="alert {{message.tags}} alert-dismissible" role="alert">

        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="True">&times;</span>
        </button>
        {{message}}
        </div>
        </div>
    {% endfor %}
