from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^all-posts/',views.post,name='post'),
    url(r'^new_post/',views.new_post,name="new_post"),
    url(r'^rmyposts/',views.myposts,name="myposts"),
    url(r'^editpost /(?P<slug>[-\w]+)/?',views.editpost,name="editpost"),
    url(r'^deletepost /(?P<slug>[-\w]+)/?',views.deletepost,name="deletepost"),
    url(r'^post /(?P<slug>[-\w]+)/?',views.clickOnPost,name='clickPost'),
    url(r'^search/',views.SearchResultsView.as_view(),name="search")
]
