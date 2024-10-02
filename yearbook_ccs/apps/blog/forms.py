from django import forms

class BlogForm(forms.Form):
    post_msg = forms.CharField(widget=forms.Textarea)
    media = forms.FileField(required=False)
