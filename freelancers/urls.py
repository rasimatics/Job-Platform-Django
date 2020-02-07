from django.urls import path
from . import views

urlpatterns = [
    path('freelancers/',views.freelancers,name="freelancers")

]
