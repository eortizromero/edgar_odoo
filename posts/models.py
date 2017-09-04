# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
	titulo 		= models.CharField(max_length=120)
	contenido 	= models.TextField()
	creado		= models.DateTimeField(auto_now=False, auto_now_add=True)
	actualizado	= models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.titulo

	def __str__(self):
		return self.titulo