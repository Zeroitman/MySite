from django.db import models


class Program:
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, blank=True, null=True)
    # child_id related to Child model, delete Cascade
    # author_therapist_id related to User model delete Cascade
    # attending_therapist_id related to User model delete Cascade
