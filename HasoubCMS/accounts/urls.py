from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

# app_name="accounts"



urlpatterns=[
    path('register/',views.register_request,name='register'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('',views.home_page,name='homepage'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('add_class/',views.add_class,name='addclass'),
    path('add_course/',views.add_course,name='addcourse'),
    path('edit_course/<int:id>',views.edit_course,name='editcourse'),
    path('delete_course/<int:id>',views.delete_course,name='deletecourse')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)