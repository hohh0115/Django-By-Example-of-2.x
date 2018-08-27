from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
	"""
	the base class of Form
	"""
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
	"""
	the base class of ModelForm
	"""
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')
