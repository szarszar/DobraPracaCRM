from django.forms import ModelForm, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import *


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
        exclude = ('client',)
        widgets = {'employees': forms.widgets.CheckboxSelectMultiple()}


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
