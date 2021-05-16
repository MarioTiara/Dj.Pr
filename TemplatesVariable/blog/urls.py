from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^stories/$',views.stories),
    url(r'^news/$',views.news),
    url(r'^$',views.index),
]