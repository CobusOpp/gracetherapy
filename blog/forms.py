from django import forms
from tinymce.widgets import TinyMCE
from .models import Comment

class CommentForm(forms.ModelForm):
	body = forms.CharField(widget=TinyMCE(), label='Comment')
	class Meta:
		model = Comment
		fields = ['name', 'body']
