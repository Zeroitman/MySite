from webapp.models import Session, Child, UserInfo, Program, Result
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

    class Meta:
        model = Session
        fields = ['program', 'child', 'attending_therapist', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = ["created_date", "edited_date", "deleted_date"]


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["done", "done_with_hint"]
