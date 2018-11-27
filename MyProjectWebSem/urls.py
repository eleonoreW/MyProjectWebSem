"""MyProjectWebSem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.views.defaults import page_not_found

from MyProjectWebSem import views

urlpatterns = [
    url(r'^Recipes/', include('Recipes.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^contact', views.contact, name='contact'),
    path('accounts/', include('accounts.urls')),
    url(r'^diets/', views.diets, name='diets'),
    url(r'^regime1/', views.regime1, name='regime1'),
    url(r'^regime2/', views.regime2, name='regime2'),
    url(r'^regime3/', views.regime3, name='regime3'),
    url(r'^regime4/', views.regime4, name='regime4'),
    url(r'^regime5/', views.regime5, name='regime5'),
    url(r'^regime6/', views.regime6, name='regime6'),
    url(r'^regime7/', views.regime7, name='regime7'),
    url(r'^regime8/', views.regime8, name='regime8'),
    url(r'^regime9/', views.regime9, name='regime9'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'', views.home, name='home'),
    url(r'', views.cookbook, name='cookbook'),
    url(r'^404/$', page_not_found, {'exception': Exception()})
]