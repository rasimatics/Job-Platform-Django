from django.urls import path
from . import views

urlpatterns = [
    path('freelancers/', views.freelancers, name="freelancers"),
    path('add/', views.addFreelancer, name="add"),
    path('edit/', views.editFreelancer, name="edit"),
    path('delete/', views.deleteFreelancer, name="delete"),
    path('detail/<slug:slug>/',views.freelancerDetail,name="detail"),
]
