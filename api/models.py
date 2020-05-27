from django.db import models
from datetime import datetime, timezone

GENDER_CHOICE=(('M', 'MACHO'),
              ('F', 'FEMEA')
              )

# this class create an object in adoptions list
class AnimalList(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    age = models.CharField(max_length=3, null=True)
    breed = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=2, null=False)
    city = models.CharField(max_length=100, null=False)
    size = models.CharField(max_length=100, null=True)
    date_rescue = models.DateField(auto_now=False, auto_now_add=False, null=True)
    gender = models.CharField(choices=GENDER_CHOICE, null=False, max_length=150)
    created_at = models.DateField(auto_now_add=True)
    mode = models.CharField(max_length=255, null=False)