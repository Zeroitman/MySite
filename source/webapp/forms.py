from webapp.models import Child, UserInfo, Program, Result, Skill
from django import forms


class SessionForm(forms.ModelForm):
    child = forms.ModelChoiceField(queryset=Child.objects.all(),
                                   empty_label='Не выбрано',
                                   widget=forms.Select(attrs={'class': 'form-control', 'required': True}),
                                   label='Ребенок')

    attending_therapist = forms.ModelChoiceField(queryset=UserInfo.objects.all(),
                                                 empty_label='Не выбрано',
                                                 widget=forms.Select
                                                 (attrs={'class': 'form-control', 'required': True}),
                                                 label='Терапист')

    program = forms.ModelMultipleChoiceField(queryset=Program.objects.all(),
                                             widget=forms.CheckboxSelectMultiple
                                             (attrs={'class': 'list-unstyled', }),
                                             label='Программы')


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


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["done", "done_with_hint"]
