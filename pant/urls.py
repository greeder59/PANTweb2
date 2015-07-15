"""PANTweb2/pant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Be sure to include this URL Configuration into PANTweb2/urls.py.
"""

from django.conf.urls import include, url
from pant import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hello/$', views.hello),
    url(r'^index/$', views.index),
    url(r'^stub/$', views.stub),
    url(r'^base/$', views.base),
    url(r'^contact/$', views.contact),
    url(r'^links/$', views.links),
    url(r'^photos/$', views.photos),
    url(r'^tour/$', views.tour),
    url(r'^directions/$', views.directions),
]