from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.post,name='post'),
    path('new_post/',views.new_post,name="new_post"),
    path('myposts/',views.myposts,name="myposts"),
    path('editpost/<int:id>/',views.editpost,name="editpost"),
    path('delete/<int:id>/',views.deletepost,name="deletepost"),
    path('post/<int:id>/',views.clickOnPost,name='clickPost'),
]
