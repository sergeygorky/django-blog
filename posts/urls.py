from django.contrib import admin
from posts import views
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.post_list),
    re_path('^create/$', views.post_create),
    re_path('^detail/$', views.post_detail),
    re_path('^update/$', views.post_update),
    re_path('^delete/$', views.post_delete),
]
