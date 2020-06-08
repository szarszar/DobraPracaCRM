from django.forms import ModelForm, FileInput
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CreateClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class CreateExpertiseForm(ModelForm):
    class Meta:
        model = Expertise
        fields = '__all__'