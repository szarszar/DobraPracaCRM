from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


def home(request):
    if request.user is not None:
        if request.user.is_staff:
            return redirect('admin_panel', 'clients')
        else:
            return redirect('panel')
    else:
        return redirect('login')


def register_employee(request):
    forms = CreateUserForm()

    if request.method == "POST":
        forms = CreateUserForm(request.POST)
        phone_number = request.POST.get('PhoneNumber', '')
        group = request.POST.get('group', '')
        if forms.is_valid():
            user = forms.save()

            Employee.objects.create(
                user=user,
                status='Active',
                phone_number=phone_number,
                group=group,

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

    context = {'projects': projects}

    return render(request, 'employee_panel.html', context)


def admin_panel(request, pk):
    clients = Client.objects.all()
    projects = Project.objects.all()
    employees = Employee.objects.all()

    context = {'clients': clients, 'projects': projects, 'employees': employees}
    if pk == 'clients':
        return render(request, 'admin_panel_clients.html', context)
    elif pk == 'projects':
        return render(request, 'admin_panel_projects.html', context)
    elif pk == 'employees':
        return render(request, 'admin_panel_employees.html', context)


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


def create_project(request, pk):
    client = Client.objects.get(id=pk)
    form = CreateProjectForm(instance=client)

    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = client
            project.save()

            return redirect('admin_panel', 'projects')

    context = {'form': form}

    return render(request, 'create_project.html', context)


def create_stage_detail(request, pk):
    project = Project.objects.get(id=pk)
    form = CreateStageDetailForm()

    if request.method == "POST":
        forms = CreateStageDetailForm(request.POST)

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

    context = {'client': client, 'projects': projects, 'form': form}
    return render(request, 'client_preview.html', context)


def project_preview(request, pk):
    project = Project.objects.get(id=pk)
    expenses = Expense.objects.filter(project=project)
    stage_details = StageDetail.objects.filter(project=project)
    client = project.client
    form = CreateProjectForm(instance=project)
    one = Employee

    if request.method == 'POST':
        form = CreateProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = client
            project.save()

            return redirect('project', pk)

    context = {'project': project, 'expenses': expenses, 'stage_details': stage_details, 'form': form}

    return render(request, 'project_preview.html', context)


def delete_object(request, pk, sc):

    thing = pk.objects.get(id=sc)
    thing.delete()


    return redirect('admin_panel', 'clients')
