from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
   url('^$', Home.as_view(), name='home'),
)