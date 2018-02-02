from django.contrib import admin
from posts import views
from django.urls import include, path, re_path
from . import views
from .views import post_create
from .views import post_detail
from .views import post_update
from .views import post_delete

urlpatterns = [
    re_path('^$', views.post_list),
    re_path('^create/$', post_create),
    re_path(r'^(?P<id>\d)/$', post_detail, name='detail'),
    re_path(r'(?P<id>\d)/edit/$', post_update, name='update'),
    re_path('^delete/$', post_delete),
]
