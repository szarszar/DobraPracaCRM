from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    status_choices = [
        ('Active', 'Active'),
        ('Not working', 'Not working'),
        ('Vacation', 'Vacation')
    ]

    group_choices = [
        ('Washer', 'Washer'),
        ('Painter', 'Painter'),
        ('Expert', 'Expert')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=24, null=True)
    status = models.CharField(max_length=12, choices=status_choices)
    group = models.CharField(max_length=10, choices=group_choices)

    def __str__(self):
        name = f"{self.user.first_name} {self.user.last_name}"
        return name


class Client(models.Model):

    company_name = models.CharField(max_length=24, blank=True)
    first_name = models.CharField(max_length=24, blank=True)
    last_name = models.CharField(max_length=24, blank=True)
    email = models.CharField(max_length=48)
    phone_number = models.CharField(max_length=48)
    city = models.CharField(max_length=24)
    address = models.CharField(max_length=24)

    def __str__(self):
        name = f"{self.company_name}{self.first_name} {self.last_name}"
        return name


class Project(models.Model):

    status_choices = [
        ('New', 'New'),
        ('Ready to wash', 'Ready to wash'),
        ('During wash', 'During wash'),
        ('Ready to paint', 'Ready to paint'),
        ('In painting', 'In painting'),
        ('Finished', 'Finished'),
    ]

    advance_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),

    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    city = models.CharField(max_length=24)
    address = models.CharField(max_length=24)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=14, choices=status_choices, default="New")
    status_advance = models.CharField(max_length=14, choices=advance_choices)
    employees = models.ManyToManyField(Employee)
    update_date = models.DateField(auto_now=True)
    lift_needed = models.BooleanField(default=False)

    def __str__(self):
        name = f"{self.client.last_name} project in {self.city},{self.address}"
        return name


class StageDetail(models.Model):

    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    image_1 = models.ImageField(null=True)
    image_2 = models.ImageField(null=True)
    image_3 = models.ImageField(null=True)
    image_4 = models.ImageField(null=True)


class Expense(models.Model):

    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField(null=True)
    cost = models.IntegerField()





