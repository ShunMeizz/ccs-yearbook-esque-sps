from django import forms
from .models import Blog, Comment
from django.forms import ClearableFileInput

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'media')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control m-1'}),
            'content': forms.Textarea(attrs={'placeholder': 'What\'s on your mind?', 'class': 'form-control m-1'}),
            'media': ClearableFileInput(attrs={'class': 'form-control m-1'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder':'Write a comment'}),
        }