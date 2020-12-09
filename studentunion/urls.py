"""studentunion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from union import views as union_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('union.urls')),
    path('accounts/register',user_views.register_user,name='register_user'),
    path('accounts/login',user_views.user_login,name='user_login'),
    path('logout', user_views.user_logout, name='user_logout'),
]
