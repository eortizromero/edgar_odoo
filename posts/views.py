# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


def crear_post(request):
	return HttpResponse('Add Post')

def mostrar_post(request):
	return HttpResponse('Detail Post')

def listar_post(request):
	if request.user.is_authenticated():
		contexto = {
			'titulo': 'JBR Account Connected ...'
		}
	else:
		contexto = {
			'titulo': 'You are not logued in your JBR ACCOUNT'
		}
	return render(request, 'index.html', contexto)

def actualizar_post(request):
	return HttpResponse('Update Post')

def eliminar_post(request):
	return HttpResponse('Delete Post')