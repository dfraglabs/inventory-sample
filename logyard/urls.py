from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_logs$', display_logs, name='display_logs'),
    url(r'^display_plywood$', display_plywood, name='display_plywood'),
]
