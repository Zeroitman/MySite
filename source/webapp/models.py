from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='client', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон пользователя')
    child = models.ManyToManyField('Child', related_name='user_child', verbose_name='Ребенок')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата редактирования')

    def __str__(self):
        return "%s. %s %s" % (self.user.id, self.user.first_name, self.user.last_name)


class Child(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя ребенка')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия ребенка')
    third_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество ребенка')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    age = models.CharField(max_length=100, verbose_name='Возраст')
    address = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Адрес проживания')
    characteristic = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Характеристика на ребенка')
    preferences = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Предпочтения ребенка')
    first_parent = models.CharField(max_length=255, verbose_name='Родитель')
    second_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name='Родитель')
    contacts = models.CharField(max_length=200, blank=True, null=True, verbose_name='Контакты ребенка')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления ребенка')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')

    def __str__(self):
        return "%s. %s %s" % (self.id, self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Дети'
        verbose_name_plural = 'Дети'


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    code_category = models.CharField(max_length=50, null=True, blank=True, verbose_name='Код категории')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Время редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Время удаления')

    def __str__(self):
        return "%s. %s" % (self.code_category, self.name)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Skill(models.Model):
    code_skill = models.CharField(max_length=5, verbose_name='Код навыка')
    name = models.CharField(max_length=255, verbose_name='Название навыка')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='skill', verbose_name='Категория')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание навыка')
    criterion = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Критерии')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания навыка')
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True,
                                        verbose_name='Время редактирование навыка')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Время удаления навыка')

    def __str__(self):
        return "%s. %s" % (self.code_skill, self.name)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class SkillsInProgram(models.Model):
    program = models.ForeignKey('Program', related_name='related_to_program', on_delete=models.PROTECT,
                                verbose_name='Программа')
    skill = models.ForeignKey('Skill', related_name='skill_in_program', on_delete=models.PROTECT,
                              verbose_name='Навык')
    status = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return "Навык %s" % self.id


class Program(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название программы")
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание программы")
    child = models.ForeignKey('Child', on_delete=models.PROTECT, related_name='child_in_program',
                              verbose_name='Ребенок')
    author_therapist = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='author_program',
                                         verbose_name='Терапист')
    skills = models.ManyToManyField('Skill', through='SkillsInProgram', verbose_name='Навыки')
    status = models.BooleanField(default=True, verbose_name='Статус')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    def __str__(self):
        return "%s %s - программа №%s" % (self.child.first_name, self.child.last_name, self.id)

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'


class Session(models.Model):
    program = models.ForeignKey(Program, related_name='session_program', on_delete=models.PROTECT,
                                verbose_name='Программа')
    attending_therapist = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='attending_session')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание сессии")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    def __str__(self):
        return "Сессия %s" % self.id

    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'


class Result(models.Model):
    session = models.ForeignKey(Session, on_delete=models.PROTECT, related_name='session_results')
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, related_name='skills_results')
    done = models.PositiveSmallIntegerField(default=0)
    done_with_hint = models.PositiveSmallIntegerField(default=0)
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата редактирования")
    deleted_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")

    def __str__(self):
        return "Результаты к сессии %s" % self.session.id

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
