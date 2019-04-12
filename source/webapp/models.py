from django.db import models


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
