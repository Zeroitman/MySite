from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    code_category = models.CharField(max_length=50, null=True, blank=True, verbose_name='Код категории')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Время редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Время удаления')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Skill(models.Model):
    code_skill = models.CharField(max_length=5, verbose_name='Код навыка')
    name = models.CharField(max_length=255, verbose_name='Название навыка')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='skill')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание навыка')
    criterion = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Критерии')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания навыка')
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True,
                                        verbose_name='Время редактирование навыка')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Время удаления навыка')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='client', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон пользователя')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата редактирования')

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Child(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя ребенка')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия ребенка')
    third_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество ребенка')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    age = models.CharField(max_length=100, verbose_name='Возраст')
    address = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Адрес проживания')
    characteristic = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Характеристика на ребенка')
    preferences = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Предпочтения ребенка')
    contacts = models.CharField(max_length=200, blank=True, null=True, verbose_name='Контакты ребенка')
    first_parent = models.ForeignKey(UserInfo, on_delete=models.PROTECT,
                                     related_name="fp_child", verbose_name='Родитель')
    second_parent = models.ForeignKey(UserInfo, on_delete=models.PROTECT, blank=True, null=True, related_name='sp_child')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления ребенка')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')

    class Meta:
        verbose_name = 'Дети'
        verbose_name_plural = 'Дети'


class Program(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название программы")
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание программы")
    author_therapist = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='author_program')
    skill = models.ManyToManyField(Skill, related_name='skill_program')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'


class Session(models.Model):
    program = models.ForeignKey(Program, verbose_name='Программа',
                                on_delete=models.PROTECT, related_name='session_program')
    child = models.ForeignKey(Child, on_delete=models.PROTECT, related_name="session_child", verbose_name='Имя ребенка')
    attending_therapist = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='attending_session')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание сессии")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'


class Result(models.Model):
    DONE = 'done'
    DONE_WITH_HINT = 'with_hint'
    NO_ANSWER = 'no_answer'

    STATUS_CHOICES = (
        (DONE, 'Выполнено'),
        (DONE_WITH_HINT, 'Выполнено с подсказкой'),
        (NO_ANSWER, 'Без ответа')
    )

    session = models.ManyToManyField(Session, related_name='session_results')
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, related_name='skills_results')
    status = models.CharField(max_length=255, default=NO_ANSWER,
                              choices=STATUS_CHOICES, verbose_name="Статус результата")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
