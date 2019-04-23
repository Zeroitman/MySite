from webapp.models import Session
from django import forms


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['program', 'child', 'attending_therapist', 'description']
        widgets = {
            'program': forms.SelectMultiple(attrs={'class': 'form-control', }),
            'child': forms.Select(attrs={'class': 'form-control', }),
            'attending_therapist': forms.Select(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }






