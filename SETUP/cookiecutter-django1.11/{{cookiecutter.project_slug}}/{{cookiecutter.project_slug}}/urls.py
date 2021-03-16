"""{{cookiecutter.project_slug}} URL Mapping

The `urlpatterns` list maps URLs to views. More information:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/

Function views:
    1. Add an import:  from my_app import views
    2. Add entry to urlpatterns:  url(r'^$', views.home, name='home')

Class-based views:
    1. Add an import:  from my_app.views import Home
    2. Add entry to urlpatterns:  url(r'^$', Home.as_view(), name='home')

Including another (usually an app's) URLconf:
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls', namespace="blog"))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from django import VERSION

# site-wide route mapping
if VERSION[0] >= 2:
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
#        url(r'^superheroes/', include(('superheroes.urls', "superheroes"))),
    ]
else:
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        # example
#        url(r'^superheroes/', include('superheroes.urls', namespace="superheroes")),
    ]

# include Django Debug toolbar if DEBUG is set
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

## # site-wide route mapping
## urlpatterns = [
##     url(r'^admin/', admin.site.urls),
##     # example
##     # url(r'^my_app/', include('my_app.urls', namespace="myapp")),
## ]
## 
## # include Django Debug toolbar if DEBUG is set
## if settings.DEBUG:
##     import debug_toolbar
##     urlpatterns = [
##         url(r'^__debug__/', include(debug_toolbar.urls)),
##     ] + urlpatterns
