from django.db import models


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
