# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from posts.forms import PostForm
from posts.models import Post

def crear_post(request):
	form = PostForm()
	contexto = {
		'form': form,
	}
	return render(request, 'form_post.html', contexto)

def mostrar_post(request, id=None):
	# ins = Post.objects.get(id=1)
	ins = get_object_or_404(Post, id=id)
	contexto = {
		'titulo': 'Titulo',
		'ins': ins
	}
	return render(request, 'mostrar_post.html', contexto) 

def listar_post(request):
	lista = Post.objects.all()
	contexto = {
		'lista': lista
	}
	# if request.user.is_authenticated():
	# 	contexto = {
	# 		'titulo': 'JBR Account Connected ...'
	# 	}
	# else:
	# 	contexto = {
	# 		'titulo': 'You are not logued in your JBR ACCOUNT'
	# 	}
	return render(request, 'listar_post.html', contexto)

def actualizar_post(request):
	return HttpResponse('Update Post')

def eliminar_post(request):
	return HttpResponse('Delete Post')