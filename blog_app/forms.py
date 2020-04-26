from .models import Comment
from django import forms
from django.forms import ModelForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')