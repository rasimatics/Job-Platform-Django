from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^all-posts/',views.post,name='post'),
    path('new_post/',views.new_post,name="new_post"),
    path('myposts/',views.myposts,name="myposts"),
    path('editpost/<slug:slug>/',views.editpost,name="editpost"),
    path('delete/<slug:slug>/',views.deletepost,name="deletepost"),
    path('post/<slug:slug>/',views.clickOnPost,name='clickPost'),
]
