from django.contrib import admin
from .models import *



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['client', 'city', 'street', 'street_number', 'date_created']


class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['project']


admin.site.register(Expertise, ExpertiseAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)


