from webapp.models import Session, Child, UserInfo, Program, Skill
from django import forms


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['created_date', 'updated_date', 'deleted_date']
        widgets = {
            'code_skill': forms.TextInput(attrs={'class': 'form-control col-sm-10'}),
            'name': forms.TextInput(attrs={'class': 'form-control col-sm-10'}),
            'description': forms.Textarea(attrs={'class': 'form-control col-sm-10'}),
            'criterion': forms.Textarea(attrs={'class': 'form-control col-sm-10'}),
        }
