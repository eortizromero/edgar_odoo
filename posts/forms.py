# -*- coding: utf-8 -*-

from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model 	= Post
		fields 	= [
				'titulo',
				'contenido',
				]
		widgets = {
			'contenido': forms.TextInput(attrs={'class': 'materialize-textarea'})
		}

	
	# def __init__(self, *args, **kwargs):
	# 	super(PostForm, self).__init__(*args, **kwargs)
	# 	self.fields['contenido'].widget = forms.TextInput(attrs={
	# 		'class': 'materialize-textarea'
	# 		})