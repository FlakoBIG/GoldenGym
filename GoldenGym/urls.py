"""GoldenGym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GoldenGymApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.gestion_clientes,name='gestion_clientes'),
    path('encargado/',views.gestion_encargados,name='gestion_encargado'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('validar_ingreso/', views.validar_ingreso, name='validar_ingreso'),
    path('gestion_planes/', views.gestion_planes, name='gestion_planes'),
    path('eliminar_plan/<int:plan_id>/', views.eliminar_plan, name='eliminar_plan'),
    path('editar_plan/<int:plan_id>/', views.editar_plan, name='editar_plan'),
    path('registro/', views.registro_usuario, name='registro'),


]
