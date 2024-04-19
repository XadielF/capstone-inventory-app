"""
URL configuration for capstone_inventory_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('capstone_inventory_app.urls')),
    path('propiedades/', views.propiedad_list, name='propiedad_list'),  # URL pattern for listing properties
    path('propiedades/<int:pk>/', views.propiedad_detail, name='propiedad_detail'),  # URL pattern for retrieving property details
    path('usuarios/<int:pk>/', views.usuario_list, name='usuario_list'),  # URL pattern for listing users
]
