from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import UserAccount


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ['id_front', 'id_back', 'photo_w_id', 'school_id_number', 'email', 'username', 'password1', 'password2']
        widgets = {
            'id_front': forms.ClearableFileInput(attrs={'placeholder': 'ID Front'}),
            'id_back': forms.ClearableFileInput(attrs={'placeholder': 'ID Back'}),
            'photo_w_id': forms.ClearableFileInput(attrs={'placeholder': 'Photo with ID'}),
            'school_id_number': forms.TextInput(attrs={'placeholder': 'School ID Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['confirm_password']:
                self.fields[field].widget.attrs['placeholder'] = field.capitalize()

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")

        return cleaned_data


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
