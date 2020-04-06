from django.conf.urls import url
from django.urls import path, re_path
from . import views


urlpatterns = [
    url(r'^freelancers/?', views.freelancers, name="freelancers"),
    url(r'^add/?', views.addFreelancer, name="add"),
    url(r'^edit/?', views.editFreelancer, name="edit"),
    url(r'^delete/?', views.deleteFreelancer, name="delete"),
    url(r'^detail /(?P<slug>[-\w]+)/?',views.freelancerDetail,name="detail"),
    url(r'^freelancersearch/?', views.SearchResultsFreelancer.as_view() , name="freelancersearch")
]
