# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.listar_post, name='listar_post'),
	url(r'^crear/$', views.crear_post, name='crear_post'),
	url(r'^mostrar/$', views.mostrar_post, name='mostrar_post'),
	url(r'^actualizar/$', views.actualizar_post, name='actualizar_post'),
	url(r'^eliminar/$', views.eliminar_post, name='eliminar_post'),
]