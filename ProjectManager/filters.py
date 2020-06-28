import django_filters
from .models import *
from django_filters import DateFromToRangeFilter


class ProjectFilter(django_filters.FilterSet):
    date = DateFromToRangeFilter(field_name='date_created')
    date_updated = DateFromToRangeFilter(field_name='update_date')

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(ProjectFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['client'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['city'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['address'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['status'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['employees'].field.widget.attrs.update({'class': 'custom-select'})
        self.filters['client'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['lift_needed'].field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['description', 'status_advance', 'date_created', 'update_date']


class ClientFilter(django_filters.FilterSet):

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(ClientFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['company_name'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['email'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['phone_number'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['city'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['address'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['zip_code'].field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Client
        fields = '__all__'


class EmployeeFilter(django_filters.FilterSet):

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(EmployeeFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['group'].field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Employee
        fields = ['group']
