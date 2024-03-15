"""
URL configuration for cert_project project.

"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('app_1.urls')),
    path('', include("allauth.urls")),

]
