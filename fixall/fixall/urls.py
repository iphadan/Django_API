"""
URL configuration for fixall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include 
from django.conf import settings
from home import routers as home_api_router
api_auth_patterns=[path('',include('rest_framework_social_oauth2.urls')),]
if settings.DEBUG:
    api_auth_patterns.append(path(r'verify/',include('rest_framework.urls'))),
    

api_url_patterns=[
    path(r'auth/',include(api_auth_patterns)),
    path(r'home/',include(home_api_router.router.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(api_url_patterns))
    
]
