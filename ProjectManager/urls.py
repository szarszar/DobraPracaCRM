from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('panel/', views.panel, name='panel'),
    path('admin_panel/<str:pk>', views.admin_panel, name='admin_panel'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_employee, name='register'),
    path('create_client/', views.create_client, name='create_client'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_expertise/<str:pk>', views.create_expertise, name='create_expertise'),
    path('client_preview/<str:pk>', views.client_preview, name='client'),
    path('project_preview/<str:pk>', views.project_preview, name='project')



]