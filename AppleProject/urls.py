"""AppleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app import views
from app.views import signin, address, authentification, gopay, paylead, lead, update_successful

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^authentification/$', views.authentification, name='authentification'),
    url(r'^address/$', views.address, name='address'),
    url(r'^gopay/$', views.gopay, name='gopay'),
    url(r'^paylead/$', views.paylead, name='paylead'),
    url(r'^lead/$', views.lead, name='lead'),
    url(r'^update_successful/$', views.update_successful, name='update_successful'),
]
