from django.db import models
from django.contrib.auth.models import User


class Children(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=100)
    address = models.TextField(max_length=1000, blank=True, null=True)
    characteristic = models.CharField(max_length=1000, blank=True, null=True)
    preferences = models.CharField(max_length=1000, blank=True, null=True)
    contacts = models.CharField(max_length=200, blank=True, null=True)
    # first_parent = models.ForeignKey() TODO required#id
    # second_parent = models.ForeignKey() TODO
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    delete_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return "%s %s, %s" % (self.first_name, self.last_name, self.age)


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code_category = models.CharField(max_length=50, null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_date = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return self.name


class Skill(models.Model):
    code_skill = models.CharField(max_length=5, verbose_name='Код навыка', default="Введите код навыка!")
    name = models.CharField(max_length=255, verbose_name='Название навыка')
    # code_category = models.ForeignKey// привязать к модели Категории
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание навыка')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания навыка')
    date_update = models.DateTimeField(null=True, blank=True, verbose_name='Время редактирование навыка')
    date_delete = models.DateTimeField(null=True, blank=True, verbose_name='Время удаления навыка')

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='client', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    delete_date = models.DateTimeField()
    edit_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, blank=True, null=True)
    # child_id related to Child model, delete Protect
    # author_therapist_id related to User model delete Protect
    # attending_therapist_id related to User model delete Protect
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    program = models.ForeignKey(Program, verbose_name='Программа', on_delete=models.PROTECT)
    description = models.TextField(max_length=2000, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.program


class Results(models.Model):
    DONE = 'done'
    DONE_WITH_HINT = 'done with hint'
    NO_ANSWER = 'no answer'

    STATUS_CHOICES = (
        (DONE, 'done'),
        (DONE_WITH_HINT, 'done with hint'),
        (NO_ANSWER, 'no answer')
    )

    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.PROTECT)
    status = models.CharField(max_length=255, default=NO_ANSWER, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Сессия %s,  навык %s' % (self.session_id, self.skill.code_skill)
