from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    id_front = forms.FileField(required=True)
    id_back = forms.FileField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customizing the widgets for each field
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'required': True,
            'placeholder': 'John Doe',
            'maxlength': '16',
            'minlength': '6',
        })
        
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'required': True,
            'placeholder': 'JohnDoe@mail.com',
        })
        
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-input',
            'required': True,
            'placeholder': 'John',
        })
        
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-input',
            'required': True,
            'placeholder': 'Doe',
        })
        
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'required': True,
            'placeholder': 'Password',
            'maxlength': '22',
            'minlength': '8',
        })
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'required': True,
            'placeholder': 'Confirm Password',
            'maxlength': '22',
            'minlength': '8',
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'id_front', 'id_back']
