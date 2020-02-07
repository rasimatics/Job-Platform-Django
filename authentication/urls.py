from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('signup/', views.register, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change_passwd.html',
            success_url='/'
        ),
        name='change-password'
    )
]
