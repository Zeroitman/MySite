from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    code_category = models.CharField(max_length=50, null=True, blank=True, verbose_name='Код категории')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Время редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Время удаления')

    def _str_(self):
        return "%s, Код категории: %s" % (self.name, self.code_category)


class Skill(models.Model):
    code_skill = models.CharField(max_length=5, verbose_name='Код навыка')
    name = models.CharField(max_length=255, verbose_name='Название навыка')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='skill')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание навыка')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания навыка')
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Время редактирование навыка')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Время удаления навыка')

    def __str__(self):
        return '%s Код навыка: %s' % (self.name, self.code_skill)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='client', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон пользователя')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата редактирования')

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Children(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя ребенка')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия ребенка')
    third_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество ребенка')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    age = models.CharField(max_length=100, verbose_name='Возраст')
    address = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Адрес проживания')
    characteristic = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Характеристика на ребенка')
    preferences = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Предпочтения ребенка')
    contacts = models.CharField(max_length=200, blank=True, null=True, verbose_name='Контакты ребенка')
    first_parent = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='fp_child')
    second_parent = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.PROTECT, related_name='sp_child')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления ребенка')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')

    def __str__(self):
        return "%s %s, %s" % (self.first_name, self.last_name, self.age)


class Program(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название программы")
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание программы")
    child = models.ForeignKey(Children, on_delete=models.PROTECT, related_name="child_program")
    author_therapist = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='author_program')
    attending_therapist = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='attending_program')
    skill = models.ManyToManyField(Skill, related_name='skill_program')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    def __str__(self):
        return "Название программы: %s, Исполнитель %s" % (self.name, self.attending_therapist.user.last_name)


class Session(models.Model):
    program = models.ForeignKey(Program, verbose_name='Программа', on_delete=models.PROTECT)
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание сессии")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    def __str__(self):
        return 'Сессия номер: %s, Программа: %s, Создано %s' % (self.id, self.program.name, self.created_date)


class Results(models.Model):
    DONE = 'done'
    DONE_WITH_HINT = 'with_hint'
    NO_ANSWER = 'no_answer'

    STATUS_CHOICES = (
        (DONE, 'Выполнено'),
        (DONE_WITH_HINT, 'Выполнено с подсказкой'),
        (NO_ANSWER, 'Без ответа')
    )

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='session_results')
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, related_name='skills_result')
    status = models.CharField(max_length=255, default=NO_ANSWER,
                              choices=STATUS_CHOICES, verbose_name="Статус результата")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    def __str__(self):
        return 'Сессия %s,  навык %s' % (self.session.id, self.skill.code_skill)
