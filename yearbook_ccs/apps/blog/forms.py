from django import forms
from .models import Blog
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
        
PROGRAM = (
    ("BSCS","Computer Science"),
    ("BSIT","Information Technology")
)

class FilterForm(forms.Form):
    prog = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PROGRAM,
    )
