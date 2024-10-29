from django import forms
from .models import Comment, ProfileComment, BlogComment

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write a comment', 'rows': 2, 'required': True})
        }

class ProfileCommentCreationForm(CommentCreationForm):
    class Meta:
        model = ProfileComment
        fields = CommentCreationForm.Meta.fields
    
class BlogCommentCreationForm(CommentCreationForm):
    class Meta:
        model = BlogComment
        fields = CommentCreationForm.Meta.fields