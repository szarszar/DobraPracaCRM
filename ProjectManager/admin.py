from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user',]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['client', 'city', 'address', 'date_created']


class StageDetailAdmin(admin.ModelAdmin):
    list_display = ['project']


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['project', 'cost']

class StageDetailImagesAdmin(admin.ModelAdmin):
    list_display = ['stage_detail']


admin.site.register(StageDetail, StageDetailAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(StageDetailImages, StageDetailImagesAdmin)


