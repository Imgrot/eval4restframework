"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from taller import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('ver_json/', views.ver_json),
    path('miembro_detalle/<int:id>', views.miembros_detalle),
    path('miembro_ver/', views.miembros_list),
    path('memberList/', views.MiembroList.as_view()),
    path('memberDetail/<int:pk>', views.MiembroDetalle.as_view()),
]
