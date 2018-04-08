"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls import include, url
from . import views

from account.views import (
    login_view,
    logout_view,
    register_view,
    profile_view,
    save,
    list)

urlpatterns = [
    url(r'^substitution/$', list, name="substitution"),
    url(r'^save/$', save, name="save_product"),
    url(r'^register/$', register_view, name="register"),
    url(r'^profile/$', profile_view, name="profile"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
]