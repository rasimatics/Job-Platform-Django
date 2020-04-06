from django.conf.urls import url
from django.urls import path, re_path
from .views import Jobs,JobDetail,JobCreate,JobDelete,MyJobs,JobUpdate,SearchResultsJobs




urlpatterns = [
    url(r'^jobs/?', Jobs.as_view(), name="alljobs"),
    url(r'^job-create/?', JobCreate.as_view(), name="jobcreate"),
    url(r'^job-detail /(?P<slug>[-\w]+)/?', JobDetail.as_view(),name="jobdetail"),
    url(r'^job-update /(?P<slug>[-\w]+)/?',JobUpdate.as_view(),name="jobupdate"),
    url(r'^job-delete /(?P<slug>[-\w]+)/?',JobDelete.as_view(),name="jobdelete"),
    url(r'^myjobs/?',MyJobs.as_view(),name="myjobs"),
    url(r'^jobsearch/?', SearchResultsJobs.as_view(), name='jobsearch')
]
