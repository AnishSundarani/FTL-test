from django.urls import path, include
from django.conf import settings
from user.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'data', views.UserData)

urlpatterns = [
    path('getdata/', views.get_users),
    path('', include(router.urls)),
]
