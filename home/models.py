from distutils import dep_util
from unicodedata import name
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    desig = models.CharField(max_length=50)
    salary = models.IntegerField()