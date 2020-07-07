from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['client', 'date_created']


class StageDetailAdmin(admin.ModelAdmin):
    list_display = ['project']


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['project', 'cost']


class StageDetailImagesAdmin(admin.ModelAdmin):
    list_display = ['stage_detail']


class ValuationAdmin(admin.ModelAdmin):
    list_display = ['client']


class MeetingAdmin(admin.ModelAdmin):
    list_display = ['valuation']


admin.site.register(StageDetail, StageDetailAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(StageDetailImages, StageDetailImagesAdmin)
admin.site.register(Valuation, ValuationAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(ValuationDetails)
admin.site.register(ValuationImages)
admin.site.register(Expert)

