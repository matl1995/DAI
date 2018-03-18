# restaurantes/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^svg/$', views.svg, name='svg'),
    url(r'^restaurantes/$', views.restaurantes, name='restaurantes'),
    url(r'^getpagina/$', views.getpagina, name='getpagina'),
    url(r'^modificarrestaurante/$', views.modificarrestaurante, name='modificarrestaurante'),
    url(r'^aniadirrestaurante/$', views.aniadirrestaurante, name='aniadirrestaurante'),
    url(r'^getgrafico/$', views.getgrafico, name='getgrafico'),
]