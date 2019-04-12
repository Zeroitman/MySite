from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code_category.Charfield(max_length=50, null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_date = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return self.name