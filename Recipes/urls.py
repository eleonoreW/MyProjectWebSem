from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
# ex: /Recipe/5/
url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^myrecipe/', views.myrecipe, name='myrecipe'),
]