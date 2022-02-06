from operator import mod
from django.db import models

# Create your models here.

class Person(models.Model):
    checked=models.BooleanField()
    name=models.CharField(max_length=225)
    type=models.CharField(max_length=225)
    age=models.IntegerField(max_length=225)
    description=models.CharField(max_length=225)
    date=models.DateTimeField()

