from webapp.models import Child, Result, Skill
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


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = ["created_date", "edited_date", "deleted_date"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'third_name': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'age': forms.NumberInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'address': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'characteristic': forms.Textarea(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'preferences': forms.Textarea(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'first_parent': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'second_parent': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'contacts': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["done", "done_with_hint"]
