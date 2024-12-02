from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password

from .models import UserAccount

class SignUpStep1Form(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ['school_id_number', 'email', 'username', 'password1', 'password2']
        widgets = {
            'school_id_number': forms.TextInput(attrs={'placeholder': 'School ID Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your Password'}),
        }
        def __init__(self, *args, **kwargs):
            super(SignUpStep1Form, self).__init__(*args, **kwargs)
            for field in self.fields:
                if field not in ['confirm_password']:
                    self.fields[field].widget.attrs['placeholder'] = field.capitalize()

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if UserAccount.objects.filter(email=email).exists():
                self.add_error('email', 'A user with this email already exists.')
            return email
    
        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get("password1")
            password2 = cleaned_data.get("password2")

            if password1 and password2 and password1 != password2:
                self.add_error('password2', "Passwords do not match.")

            return cleaned_data

class SignUpStep2Form(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['id_front', 'id_back', 'photo_w_id']
        widgets = {
            'id_front': forms.ClearableFileInput(),
            'id_back': forms.ClearableFileInput(),
            'photo_w_id': forms.ClearableFileInput(),
        }
        
class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UpdateUserAccountForm(UserChangeForm):
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput,
        required=False
    )

    confirm_new_password = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = UserAccount
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserAccount.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            self.add_error('email', 'A user with this email already exists.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UserAccount.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            self.add_error('username', 'This username is already taken.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password")
        password2 = cleaned_data.get("confirm_new_password")

        if password1:
            try:
                password_validation.validate_password(password1, user=self.instance)
            except ValidationError as e:
                for error in e.messages:
                    self.add_error('new_password', error)

        if password1 != password2:
            self.add_error('confirm_new_password', "Passwords do not match.")

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('new_password')

        # If a new password is provided, update the password
        if new_password:
            user.password = make_password(new_password)

        if commit:
            user.save()
        return user