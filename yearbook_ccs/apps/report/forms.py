from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason',]
        widgets = {
            'reason': forms.Textarea(attrs={'placeholder': 'What is wrong here?', 'class': 'form-control m-1'}),
        }