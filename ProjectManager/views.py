from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


def home(request):

    if request.user.is_authenticated():
        return redirect('panel')
    else:
        return redirect('login')


def register_employee(request):
    forms = CreateUserForm()

    if request.method == "POST":
        forms = CreateUserForm(request.POST)
        phone_number = request.POST.get('PhoneNumber', '')
        if forms.is_valid():
            user = forms.save()
            username = forms.cleaned_data.get("username")

            Employee.objects.create(
                user=user,
                status='Active',
                phone_number=phone_number

            )
            messages.success(request, 'Konto dla ' + username + ' zostało utworzone')

            return redirect('admin_panel')

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
    return render(request, 'employee_panel.html')


def admin_panel(request):
    clients = Client.objects.all()
    projects = Project.objects.all()

    context = {'clients': clients, 'projects': projects}
    return render(request, 'admin_panel.html', context)


def create_client(request):
    form = CreateClientForm()

    if request.method == "POST":
        forms = CreateClientForm(request.POST)
        if forms.is_valid():
            forms.save()

            return redirect('admin_panel')

    context = {'form': form}

    return render(request, 'create_client.html', context)


def create_project(request):
    form = CreateProjectForm()

    if request.method == "POST":
        forms = CreateProjectForm(request.POST)
        if forms.is_valid():
            forms.save()

            return redirect('admin_panel')

    context = {'form': form}

    return render(request, 'create_project.html', context)


def create_expertise(request):
    form = CreateExpertiseForm()

    if request.method == "POST":
        forms = CreateExpertiseForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()

            return redirect('admin_panel')

    context = {'form': form}

    return render(request, 'create_expertise.html', context)


def client_preview(request, pk):

    client = Client.objects.get(id=pk)
    projects = Project.objects.filter(client=client)

    context = {'client': client, 'projects': projects}
    return render(request, 'client_preview.html', context)


def project_preview(request,pk):

    project = Project.objects.get(id=pk)
    expertise = Expertise.objects.filter(project=project)

    context = {'project': project, 'expertise': expertise}
    return render(request, 'project_preview.html', context)

