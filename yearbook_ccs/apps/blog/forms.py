from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','content','media')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Title'}),
            'content': forms.Textarea(attrs={'placeholder':'Whats on your mind'}),
        }