from django.urls import path
from .views import Jobs,JobDetail,JobCreate,JobDelete,MyJobs,JobUpdate

urlpatterns = [
    path('all-jobs/', Jobs.as_view(), name="alljobs"),
    path('job-create/', JobCreate.as_view(), name="jobcreate"),
    path('job-detail/<int:pk>', JobDetail.as_view(),name="jobdetail"),
    path('job-update/<int:pk>',JobUpdate.as_view(),name="jobupdate"),
    path('job-delete/<int:pk>',JobDelete.as_view(),name="jobdelete"),
    path('myjobs/',MyJobs.as_view(),name="myjobs"),
]
