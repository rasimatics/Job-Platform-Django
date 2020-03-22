from django.urls import path
from . import views

urlpatterns = [
    path('all-jobs/', views.Jobs.as_view(), name="alljobs"),
    path('job-detail/<int:pk>',views.JobDetail.as_view(),name="jobdetail"),
    # path('job-create/', views.JobCreate.as_view(), name="job-create"),

]
