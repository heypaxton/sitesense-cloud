"""sitesense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.views import password_reset


from rest_framework import routers

from cmdsenseapi import views

router = routers.DefaultRouter()
# router.register(r'reading', views.ReadingViewSet)

urlpatterns = [
    # url(r'^', include('django.contrib.auth.urls')),
    url(r'^readings/read/$', views.read),
    url(r'^readings/read_position/$', views.read_position),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^forget_password/$', views.forget_password, name='forget_password'),
    url(r'^confirm_mail/$', views.confirm_mail, name='confirm_mail'),
    url(r'^register/$', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),

    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
