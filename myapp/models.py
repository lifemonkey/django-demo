from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    contact = models.IntegerField
    email = models.EmailField(max_length=50)
    age = models.IntegerField
    file = models.FileField

    class Meta:
        db_table = "student"
