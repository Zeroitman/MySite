from django.db import models


class Children(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(auto_now_add=False, null=True, blank=True)
    age = models.IntegerField()
    address = models.CharField(max_length=200, blank=True, null=True)
    characteristic = models.CharField(max_length=1000, blank=True, null=True)
    preferences = models.CharField(max_length=1000, blank=True, null=True)
    # first_parent = models.ForeignKey() TODO
    # second_parent = models.ForeignKey() TODO
    add_date = models.DateField(auto_now=True)
    edit_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s, %s" % (self.first_name, self.last_name, self.age)
