from webapp.models import Session, Child, UserInfo, Program
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
                                             (attrs={'class': 'list-unstyled',}),
                                             label='Программы')

    class Meta:
        model = Session
        fields = ['program', 'child', 'attending_therapist', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }






