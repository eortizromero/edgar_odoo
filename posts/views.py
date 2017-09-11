# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from posts.forms import PostForm
from posts.models import Post

def crear_post(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instancia = form.save(commit=False)
		instancia.save()
		messages.success(request, "Post creado correctamente")
		return HttpResponseRedirect(instancia.get_absolute_url())
	

	contexto = {
		'form'		: form,
		'titulo'	: 'Crear Nuevo Post'
	}
	return render(request, 'form_post.html', contexto)

def mostrar_post(request, id=None):
	ins = get_object_or_404(Post, id=id)
	contexto = {
		'titulo'	: ins.titulo,
		'ins'		: ins
	}
	return render(request, 'mostrar_post.html', contexto) 

def listar_post(request):
	lista = Post.objects.all()
	paginador = Paginator(lista, 5)
	pag = request.GET.get('pagina')
	try:
		posts = paginador.page(pag)
	except PageNotAnInteger:
		posts = paginador.page(1)
	except EmptyPage:
		posts = paginador.page(paginador.num_pages)

	contexto = {
		'lista'		: posts,
		'titulo'	: 'Todos los Posts',
	}

	return render(request, 'listar_post.html', contexto)

def actualizar_post(request, id=None):
	ins = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=ins)
	if form.is_valid():
		instancia = form.save(commit=False)
		instancia.save()
		messages.success(request, "Post editado correctamente") # @param extra_tag='tagname'
		return HttpResponseRedirect(instancia.get_absolute_url())
	
	contexto = {
		'titulo'	: ins.titulo,
		'ins'		: ins,
		'form'		: form
	}
	return render(request, 'form_post.html', contexto)

def eliminar_post(request, id=None):
	ins = get_object_or_404(Post, id=id)
	ins.delete()
	messages.success(request, "Post eliminado correctamente") # @param extra_tag='tagname'
	return redirect("posts:listar_post")
	