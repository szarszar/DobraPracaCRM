from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    group_choices = [
        ('Washer', 'Washer'),
        ('Painter', 'Painter'),
        ('Expert', 'Expert')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=24, null=True)
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
    zip_code = models.CharField(max_length=6, null=True)

    def __str__(self):
        name = f"{self.company_name} {self.first_name} {self.last_name}"
        return name


class Valuation(models.Model):

    def file_path(self):
        return '{0}'.format(self.client.last_name)

    status_choices = [
        ('New', 'New'),
        ('Meeting was arranged', 'Meeting was arranged'),
        ('Offer sent', 'Offer sent'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=24, choices=status_choices)
    offer_file = models.FileField(upload_to=file_path, blank=True, null=True)
    message = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class ValuationDetails(models.Model):
    layers_choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]

    valuation = models.ForeignKey(Valuation, on_delete=models.CASCADE)
    surface_area = models.DecimalField(max_digits=6, decimal_places=2)
    number_of_layers = models.IntegerField(choices=layers_choices)
    employees_needed = models.IntegerField(choices=layers_choices)
    work_hours = models.SmallIntegerField()
    lift_needed = models.BooleanField(default=False)


class Meeting(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    valuation = models.ForeignKey(Valuation, on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=20, null=True)
    time = models.CharField(max_length=6, null=True)
    city = models.CharField(max_length=24, null=True)
    address = models.CharField(max_length=24, null=True)
    zip_code = models.CharField(max_length=6, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)


class ValuationImages(models.Model):
    valuation = models.ForeignKey(Valuation, on_delete=models.CASCADE)
    image = image = models.FileField(upload_to="images/")


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
    status_advance = models.CharField(max_length=14, choices=advance_choices, blank=True)
    employees = models.ManyToManyField(Employee)
    update_date = models.DateField(auto_now=True, blank=True)
    lift_needed = models.BooleanField(default=False)
    description = models.TextField(null=True)

    def __str__(self):
        name = f"{self.client.last_name} project in {self.city},{self.address}"
        return name


class StageDetail(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    status = models.CharField(max_length=14, default="New")

    def __str__(self):
        name = f"Detail for {self.project.status} stage"
        return name


class Expense(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField(null=True)
    cost = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    def __str__(self):
        name = f"Expense nr {self.id} for {self.project}"
        return name


class StageDetailImages(models.Model):
    stage_detail = models.ForeignKey(StageDetail, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
