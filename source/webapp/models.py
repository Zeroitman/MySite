from django.db import models
from django.contrib.auth.models import User


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
