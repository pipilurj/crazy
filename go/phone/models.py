from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Phone(models.Model):
    number = models.CharField(max_length=30)
    shit = models.CharField(max_length=30)