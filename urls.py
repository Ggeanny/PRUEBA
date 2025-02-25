"""
URL configuration for FerreLink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from FerreMaster import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('new', views.item_create, name='item_create'),
    path('edit/<int:id>/', views.item_update, name='item_update'),
    path('delete/<int:id>/', views.item_delete, name='item_delete'),
]
