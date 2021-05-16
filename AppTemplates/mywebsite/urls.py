from django.conf import urls
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url (r'^blog/',include('blog.urls')),
    url(r'^about/',include('about.urls')),
    url(r'^$',views.index)
]
