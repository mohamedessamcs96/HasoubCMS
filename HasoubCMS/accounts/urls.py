from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

# app_name="accounts"



urlpatterns=[
    path('register/',views.register_request,name='register'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('',views.home_page,name='homepage'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)