from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    status_choices = [
        ('Active', 'Active'),
        ('Not working', 'Not working'),
        ('Vacation', 'Vacation')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=24, null=True)
    status = models.CharField(max_length=12, choices=status_choices)

    def __str__(self):
        name = f"{self.user.first_name} {self.user.last_name}"
        return name


class Client(models.Model):

    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.CharField(max_length=48)
    city = models.CharField(max_length=24)
    street = models.CharField(max_length=24)
    street_number = models.CharField(max_length=10)

    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        return name


class Project(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    city = models.CharField(max_length=24)
    street = models.CharField(max_length=24)
    street_number = models.CharField(max_length=10)
    employee = models.ManyToManyField(Employee)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = f"{self.client.last_name} project in {self.city}"
        return name


class Expertise(models.Model):

    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    description = models.TextField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()






