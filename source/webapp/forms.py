from webapp.models import Session
from django import forms


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        exclude = ['created_date', 'edited_date', 'deleted_date']





