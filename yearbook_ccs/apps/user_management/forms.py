from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserAccount


class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = UserAccount
        fields = "__all__"
        widgets = {
            'id_front': forms.ClearableFileInput(attrs={'placeholder': 'ID Front'}),
            'id_back': forms.ClearableFileInput(attrs={'placeholder': 'ID Back'}),
            'photo_w_id': forms.ClearableFileInput(attrs={'placeholder': 'Photo with ID'}),
            'school_id_number': forms.TextInput(attrs={'placeholder': 'School ID Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['confirm_password']:
                self.fields[field].widget.attrs['placeholder'] = field.capitalize()


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
