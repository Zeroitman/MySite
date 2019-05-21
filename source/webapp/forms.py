from webapp.models import Child, UserInfo, Result, Skill, Program, Categories, SkillsInProgram
from django import forms
from django_select2.forms import Select2MultipleWidget
import datetime


class SkillForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(),
                                      empty_label='Не выбрано...',
                                      widget=forms.Select
                                      (attrs={'class': 'form-control form-control-sm shadow-none', 'required': True}),
                                      label='Категория', )

    class Meta:
        model = Skill
        exclude = ['created_date', 'updated_date', 'deleted_date']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid',
                       'placeholder': 'Название навыка', 'required': True}),
            'code_skill': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid',
                       'placeholder': 'Код навыка', 'required': True}),
            'skill_comment': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Комментарий к навыку'}),
            'description':forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Описание навыка'}),
            'criterion': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Критерий навыка'}),
        }


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = ["created_date", "edited_date", "deleted_date", "is_deleted"]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid',
                       'placeholder': 'Имя ребенка', 'required': True}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid',
                       'placeholder': 'Фамилия ребенка', 'required': True}),
            'third_name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Отчество ребенка'}),
            'birthday': forms.SelectDateWidget(empty_label=('Год', 'Месяц', 'День'),
                                               years=[(r) for r in range(1970, datetime.date.today().year + 1)],
                                               attrs={
                                                   'class': 'form-control form-control-sm '
                                                            'shadow-none w-25 d-inline-block',
                                                   'placeholder': 'Дата рождения', }),
            'age': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid', 'placeholder': 'Возраст',
                       'type': 'number', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'form-control form-control-sm shadow-none',
                                              'placeholder': 'Адрес'}),
            'characteristic': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                    'placeholder': 'Характеристика', 'rows': '3'}),
            'preferences': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Предпочтения', 'rows': '3'}),
            'first_parent': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid',
                       'placeholder': 'Первый родитель', 'required': True}),
            'second_parent': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Второй родитель'}),
            'contacts': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Контакты'}),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["done", "done_with_hint"]


class ProgramForm(forms.ModelForm):
    author_therapist = forms.ModelChoiceField(queryset=UserInfo.objects.all(),
                                              empty_label='Не выбрано...',
                                              widget=forms.Select
                                              (attrs={'class': 'form-control form-control-sm shadow-none',
                                                      'required': True}),
                                              label='Терапист')
    child = forms.ModelChoiceField(queryset=Child.objects.all(),
                                   empty_label='Не выбрано...',
                                   widget=forms.Select
                                   (attrs={'class': 'form-control form-control-sm shadow-none', 'required': True}),
                                   label='Ребёнок', )

    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(),
                                            widget=Select2MultipleWidget)

    class Meta:
        model = Program
        exclude = ["created_date", "edited_date", "deleted_date", "status"]
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Программа'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                 'placeholder': 'Описание программы', 'rows': '3'}),
            'program_comment': forms.Textarea(attrs={'class': 'form-control form-control-sm shadow-none',
                                                     'placeholder': 'Комментарий к программе', 'rows': '3'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        exclude = ["created_date", "edited_date", "deleted_date"]
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid',
                       'placeholder': 'Название категории', 'required': True}),
            'code_category': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Код категории'}),
        }


class SkillsInProgramForm(forms.ModelForm):
    class Meta:
        model = SkillsInProgram
        exclude = ["program", "status"]
        widgets = {
            'extra_skill_to_skill': forms.Select(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'skill': forms.Select(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'added_skill': forms.TextInput(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'}),
            'added_skill_comment': forms.Textarea(attrs={'class': 'form-control col-xs-12 col-sm-6 col-lg-4'})
        }
