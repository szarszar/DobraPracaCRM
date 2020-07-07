from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .filters import *
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    users = User.objects.all()
    if request.user.is_staff:
        return redirect('admin_panel', 'clients')
    elif request.user in users:
        return redirect('panel')
    else:
        return redirect('login')


@staff_member_required
def register_employee(request):
    forms = CreateUserForm()

    if request.method == "POST":
        forms = CreateUserForm(request.POST)
        phone_number = request.POST.get('PhoneNumber', '')
        if forms.is_valid():
            user = forms.save()

            employee = Employee.objects.create(
                user=user,
                phone_number=phone_number,
            )

            if request.POST.get('IsExpert', ''):
                Expert.objects.create(
                    employee=employee
                )

            messages.success(request, f"Account for {user.first_name} {user.last_name} has been created")

            return redirect('admin_panel', 'employees')

    context = {'forms': forms}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Username OR password are incorrect')
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def panel(request):
    employee = Employee.objects.get(user=request.user)
    projects = Project.objects.filter(employee=employee)

    print(meetings)
    print(employee)

    context = {'projects': projects, 'meetings': meetings}

    return render(request, 'employee_panel.html', context)


@staff_member_required
def admin_panel(request, pk):
    clients = Client.objects.all()
    projects = Project.objects.all()
    employees = Employee.objects.all()
    valuations = Valuation.objects.all()
    valuations_details = ValuationDetails.objects.all()

    filter_projects = ProjectFilter(request.GET, queryset=projects)
    projects = filter_projects.qs

    filter_clients = ClientFilter(request.GET, queryset=clients)
    clients = filter_clients.qs

    filter_employees = EmployeeFilter(request.GET, queryset=employees)
    employees = filter_employees.qs

    filter_valuations = ValuationFilter(request.GET, queryset=valuations)
    valuations = filter_valuations.qs

    filter_valuations_details = ValuationDetailFilter(request.GET, queryset=valuations_details)
    valuations_details = filter_valuations_details.qs

    context = {'clients': clients, 'projects': projects, 'employees': employees, 'valuations': valuations,
               'valuations_details': valuations_details,
               'filter_projects': filter_projects,
               'filter_clients': filter_clients, 'filter_employees': filter_employees,
               'filter_valuations_details': filter_valuations_details,
               'filter_valuations': filter_valuations}
    if pk == 'clients':
        return render(request, 'admin_panel_clients.html', context)
    elif pk == 'projects':
        return render(request, 'admin_panel_projects.html', context)
    elif pk == 'employees':
        return render(request, 'admin_panel_employees.html', context)
    elif pk == 'valuations':
        return render(request, 'admin_panel_valuations.html', context)


@staff_member_required
def create_client(request):
    form = CreateClientForm()

    if request.method == "POST":
        forms = CreateClientForm(request.POST)
        if forms.is_valid():
            client = forms.save()

            messages.success(request,
                             f"Entry for {client.company_name} {client.first_name} {client.last_name} has been created")
            return redirect('admin_panel', 'clients')

    context = {'form': form}

    return render(request, 'create_client.html', context)


@staff_member_required
def create_project(request, pk):
    valuation = Valuation.objects.get(id=pk)

    form = CreateProjectForm()

    if request.method == 'POST':
        form = CreateProjectForm(request.POST)

        print(form.errors)
        if form.is_valid():
            form = form.save(commit=False)
            form.client = valuation.client
            form.valuation = valuation
            form.status = 'New'
            form.save()

            return redirect('project', form.id)

    context = {'form': form}

    return render(request, 'create_project.html', context)


def create_stage_detail(request, pk):
    project = Project.objects.get(id=pk)
    form = CreateStageDetailForm()

    if request.method == "POST":
        forms = CreateStageDetailForm(request.POST, request.FILES)

        if forms.is_valid():
            form = forms.save(commit=False)
            form.project = project
            form.save()

        for file in request.FILES.getlist('images'):
            instance = StageDetailImages(
                stage_detail=StageDetail.objects.get(id=form.id),
                image=file
            )
            instance.save()

        return redirect('project', pk)

    context = {'form': form}

    return render(request, 'create_stage_detail.html', context)


def client_preview(request, pk):
    client = Client.objects.get(id=pk)
    form = CreateClientForm(instance=client)
    projects = Project.objects.filter(client=client)

    if request.method == "POST":
        forms = CreateClientForm(request.POST, instance=client)
        if forms.is_valid():
            client = forms.save()

            messages.success(request,
                             f"Changes for {client.company_name} {client.first_name} {client.last_name} has been saved")
            return redirect('admin_panel', 'clients')

    context = {'client': client, 'projects': projects, 'form': form}
    return render(request, 'client_edit.html', context)


def project_preview(request, pk):
    project = Project.objects.get(id=pk)
    expenses = Expense.objects.filter(project=project)
    stage_details = StageDetail.objects.filter(project=project)
    client = project.client
    form = CreateProjectForm(instance=project)
    employees = project.employees.all()

    if request.method == 'POST':
        form = CreateProjectForm(request.POST, instance=project)
        employees = request.POST.getlist('employees')

        if form.is_valid():
            project = form.save(commit=False)
            project.client = client
            project.save()
            project.employees.set(employees)

            return redirect('project', pk)

    context = {'project': project, 'expenses': expenses, 'stage_details': stage_details, 'form': form,
               'employees': employees}

    return render(request, 'project_preview.html', context)


def create_expense(request, pk):
    project = Project.objects.get(id=pk)
    form = CreateExpenseForm()

    if request.method == "POST":
        forms = CreateExpenseForm(request.POST, request.FILES)

        if forms.is_valid():
            form = forms.save(commit=False)
            form.project = project
            form.save()

        return redirect('project', pk)

    context = {'form': form}

    return render(request, 'create_expense.html', context)


def employee_panel(request):
    employee = Employee.objects.get(user=request.user)
    projects = Project.objects.filter(employees=employee)
    meetings = Meeting.objects.filter(employee=employee)

    context = {'projects': projects, 'meetings': meetings}

    return render(request, 'employee_panel.html', context)


def add_valuation(request, pk):
    client = Client.objects.get(id=pk)

    valuation = Valuation.objects.create(
        client=client,
        status='New',

    )

    return redirect('valuation', valuation.id)


def valuation_preview(request, pk):
    valuation = Valuation.objects.get(id=pk)
    form = CreateValuationForm(instance=valuation)
    meeting = Meeting.objects.filter(valuation=valuation)
    details = ValuationDetails.objects.filter(valuation=valuation)

    context = {'form': form, 'valuation': valuation, 'meeting': meeting, 'details': details}

    if details:
        images = ValuationImages.objects.filter(valuation=valuation)
        context['images'] = images

    if request.method == 'POST':
        form = CreateValuationForm(request.POST, request.FILES, instance=valuation)

        if form.is_valid():
            form = form.save(commit=False)
            form.cost = form.work_cost + form.materials_cost + form.equipment_cost
            form.save()

    return render(request, 'valuation_preview.html', context)


def add_meeting(request, pk):
    valuation = Valuation.objects.get(id=pk)
    form = CreateMeetingForm(instance=valuation.client)
    client = valuation.client

    context = {'valuation': valuation, 'form': form}

    if request.method == 'POST':
        form = CreateMeetingForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form = form.save(commit=False)
            form.client = client
            form.valuation = valuation
            valuation.status = 'Meeting was arranged'
            form.save()

        return redirect('valuation', pk)

    return render(request, 'add_meeting.html', context)


def add_valuation_details(request, pk):
    valuation = Valuation.objects.get(id=pk)
    form = ValuationDetailsForm()

    if request.method == "POST":
        forms = ValuationDetailsForm(request.POST, request.FILES)

        if forms.is_valid():
            form = forms.save(commit=False)
            form.valuation = valuation
            form.save()

            for thing in request.FILES.getlist('images'):
                instance = ValuationImages(
                    valuation=valuation,
                    image=thing
                )
                instance.save()

            return redirect('valuation', pk)

    context = {'form': form}
    return render(request, 'add_details.html', context)


def valuation_prefix(request, pk):
    client = Client.objects.get(id=pk)
    valuation = Valuation.objects.get(client=client)

    return redirect('valuation', valuation.id)
