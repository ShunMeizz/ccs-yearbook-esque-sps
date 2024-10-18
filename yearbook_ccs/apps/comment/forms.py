from django.forms import ModelForm

class CommentCreationForm(ModelForm):
    class Meta:
        fields = ['comment']
        widgets = {
            'comment': ModelForm.Textarea(attrs={'placeholder': 'Write a comment', 'rows': 2})
        }