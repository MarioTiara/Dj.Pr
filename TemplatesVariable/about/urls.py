from django.conf.urls import url 

from . import views

urlpatterns=[
    url(r'^Mario/$',views.Mario),
    url(r'^Aji/$',views.Aji),
    url(r'^Dery/$',views.Dery),
    url(r'^Ganesh/$',views.Ganesh),
    url(r'^$',views.index),
]