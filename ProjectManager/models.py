from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Employee(models.Model):

    status_choices = [
        ('Active', 'Active'),
        ('Not working', 'Not working'),
        ('Vacation', 'Vacation')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, choices=status_choices)

class Client(models.Model):

    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.CharField(max_length=48)
    city = models.CharField(max_length=24)
    street = models.CharField(max_length=24)
    street_number = models.CharField(max_length=10)


class Project(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    city = models.CharField(max_length=24)
    street = models.CharField(max_length=24)
    street_number = models.CharField(max_length=10)
    employee = models.ManyToManyField(Employee)
    date_created = models.DateTimeField(auto_now_add=True)






