"""teatrgid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from teatrgid.views import home_page, select_city, set_user_city, filter_performances

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name="home"),
    url(r'^select_city/', select_city, name="select_city"),
    url(r'^filter_performances/', filter_performances, name="filter_performances"),
    url(r'^set_user_city/(?P<city_slug>[A-z0-9_\-]+)/$', set_user_city, name="set_user_city")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
