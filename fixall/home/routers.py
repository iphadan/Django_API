from django.contrib.auth.models import User
from rest_framework import routers 
from .viewsets import UserViewSet


app_name="home"
router=routers.DefaultRouter()
router.register('users',UserViewSet)
