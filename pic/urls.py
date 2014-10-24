from django.conf.urls import patterns, url, static, include
from django.contrib import admin
from django.views.generic import TemplateView

from pic import views

urlpatterns = patterns('',
  url(r'^uploadfile/$', views.uploadpic, name='uploadpic'),
  url(r'^listfiles/$', views.displaypic, name='displaypic'),
  url(r'^afterupload/$', TemplateView.as_view(template_name='pic/afterupload.html'), name='afterupload')
)