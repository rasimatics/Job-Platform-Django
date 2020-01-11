from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('signup/', views.register, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_passwd/', views.change_passwd, name='change_passwd')
]
