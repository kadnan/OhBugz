from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^project/new/$', views.add_new_project, name='add_new_project')
]
