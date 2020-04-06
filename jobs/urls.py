from django.urls import path
from .views import Jobs,JobDetail,JobCreate,JobDelete,MyJobs,JobUpdate,SearchResultsJobs

# app_name="jobs"

urlpatterns = [
    path('all-jobs/', Jobs.as_view(), name="alljobs"),
    path('job-create/', JobCreate.as_view(), name="jobcreate"),
    path('job-detail/<slug:slug>', JobDetail.as_view(),name="jobdetail"),
    path('job-update/<slug:slug>',JobUpdate.as_view(),name="jobupdate"),
    path('job-delete/<slug:slug>',JobDelete.as_view(),name="jobdelete"),
    path('myjobs/',MyJobs.as_view(),name="myjobs"),
    path('jobsearch/', SearchResultsJobs.as_view(), name='jobsearch')
]
