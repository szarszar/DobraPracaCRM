from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Email'
        }


class CreateClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('client', 'valuation')
        widgets = {'employees_washing': forms.widgets.CheckboxSelectMultiple(),
                   'employees_painting': forms.widgets.CheckboxSelectMultiple()}


class CreateStageDetailForm(ModelForm):
    class Meta:
        model = StageDetail
        fields = '__all__'
        exclude = ('project',)


class CreateExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ('project',)


class CreateValuationForm(ModelForm):
    class Meta:
        model = Valuation
        fields = '__all__'
        exclude = ('client',)


class CreateMeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        exclude = ('client', 'valuation',)
        widgets = {
            'date': AdminDateWidget,
        }


class ValuationDetailsForm(ModelForm):
    class Meta:
        model = ValuationDetails
        fields = '__all__'
        exclude = ('valuation',)
