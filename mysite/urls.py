from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('post.urls')),
    path('', include('freelancers.urls')),
    path('', include('introduction.urls')),


]
