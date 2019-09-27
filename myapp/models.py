from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    age = models.CharField(max_length=3)
    file = models.FileField

    class Meta:
        db_table = "student"
