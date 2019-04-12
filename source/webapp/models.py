from django.db import models


class Program:
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
