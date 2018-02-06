from django.urls import re_path
from .views import post_create
from .views import post_list
from .views import post_detail
from .views import post_update
from .views import post_delete

urlpatterns = [
    re_path('^$', post_list, name='list'),
    re_path('^create/$', post_create),
    re_path(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    re_path(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<id>\d+)/delete/$', post_delete),
]
