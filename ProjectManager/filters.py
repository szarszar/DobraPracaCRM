import django_filters
from .models import *
from django_filters import DateFromToRangeFilter


class ProjectFilter(django_filters.FilterSet):
    date = DateFromToRangeFilter(field_name='date_created')
    date_updated = DateFromToRangeFilter(field_name='update_date')

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(ProjectFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['client'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['status'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['employees_washing'].field.widget.attrs.update({'class': 'custom-select'})
        self.filters['status_advance'].field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['description', 'date_created', 'update_date']


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
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ValuationFilter(django_filters.FilterSet):
    date = DateFromToRangeFilter(field_name='date_created')
    date_updated = DateFromToRangeFilter(field_name='last_update')

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(ValuationFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['client'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['status'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['message'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['cost'].field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Valuation
        fields = ['client', 'status', 'message', 'cost']


class ValuationDetailFilter(django_filters.FilterSet):

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(ValuationDetailFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['surface_area_wood'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['surface_area_concrete'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['number_of_layers'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['employees_needed'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['work_hours'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['paint_wood'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['color_code_wood'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['lift_needed'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['scaffolding_needed'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['paint_concrete'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['color_code_concrete'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['paint_windows'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['color_code_windows'].field.widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = ValuationDetails
        fields = '__all__'
        exclude = ['valuation']

