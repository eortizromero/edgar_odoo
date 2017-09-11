# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.listar_post, name='listar_post'),
	url(r'^crear/$', views.crear_post, name='crear_post'),
	url(r'^(?P<id>\d+)/$', views.mostrar_post, name='mostrar_post'),
	url(r'^(?P<id>\d+)/editar/$', views.actualizar_post, name='actualizar_post'),
	url(r'^(?P<id>\d+)/eliminar/$', views.eliminar_post, name='eliminar_post'),
]