# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
	list_display 		= ['titulo', 'creado', 'contenido', 'actualizado']
	list_display_links 	= ['actualizado']
	# list_editable 		= ['titulo']
	list_filter 		= ['actualizado', 'creado']
	search_fields 		= ['titulo', 'contenido']
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)