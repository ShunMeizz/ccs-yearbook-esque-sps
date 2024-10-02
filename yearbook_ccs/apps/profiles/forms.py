from django import forms
from .models import UserProfile
from datetime import datetime

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "program", "batch_year", "quote",
                  "hobbies", "facebook_link", "linkedin_link", "github_link", "instagram_link"]
        labels = {
            "first_name": "First Name",
            "last_name": 'Last Name', 
            "profile_pic": "Profile Picture",
            "program": "Program", 
            "quote": 'Favorite Quote',
            "hobbies": 'Hobbies', 
            "facebook_link":  'Facebook',
            "linkedin_link": 'LinkedIn',
            "github_link": "GitHub",
            "instagram_link": 'Instagram',
       
        }
        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': "First Name", 'required': 'true'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Last Name', 'required': 'true'}),
            "profile_pic": forms.ClearableFileInput(attrs={'placeholder': "Profile Picture", 'required': 'true'}),
            "program" : forms.Select(attrs={"class":'dropdown'}),
            "batch_year": forms.Select(attrs={'class': 'dropdown'}),
            "quote": forms.TextInput(attrs={'placeholder': 'Favorite Quote'}),
            "hobbies": forms.Textarea(attrs={'placeholder': 'Hobbies', 'rows': 5}),
            "facebook_link": forms.TextInput(attrs={'placeholder': 'Facebook link'}),
            "linkedin_link": forms.TextInput(attrs={'placeholder': 'LinkedIn link'}),
            "github_link": forms.TextInput(attrs={'placeholder': 'GitHub link'}),
            "instagram_link": forms.TextInput(attrs={'placeholder': 'Instagram link'}),
        }