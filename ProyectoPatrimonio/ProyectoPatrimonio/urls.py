"""
URL configuration for ProyectoPatrimonio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from core import views
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name="home"),
    
    # Rutas usando Vistas Basadas en Clases (CBV)
    path('catalogo/', views.catalogo_lugares, name='catalogo'),
    path('catalogo/categoria/<int:categoria_id>/', views.catalogo_lugares, name='catalogo_por_categoria'),
    path('lugar/<int:lugar_id>/', views.detalle_lugar, name='detalle_lugar'),
]
