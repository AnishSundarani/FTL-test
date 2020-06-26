from django.urls import path, include
from django.conf import settings
from user.api import views
from rest_framework import routers


urlpatterns = [
    path('getdata/', views.get_users),
]
