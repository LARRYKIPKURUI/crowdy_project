
"""
URL configuration for crowdy_project project.

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
from main_app import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('fundraisers/', views.fundraisers, name='fundraisers'),  # List all fundraisers
    path('donations/', views.donations, name='donations'),  # List all Donations
    path('add/fundraiser/', views.add_fundraiser, name='add_fundraiser'),  # Add a new fundraiser
    path('add/donation/<int:fundraiser_id>/', views.add_donation, name='add_donation'),  # Add donation
    path('fundraisers/delete/<int:fundraiser_id>', views.delete_fundraiser, name='delete_fundraiser'),
    path('fundraisers/details/<int:fundraiser_id>', views.fundraiser_details, name='fundraiser_details'),
    path('fundraisers/search', views.search_fundraiser, name='search_fundraiser'),
    path('fundraisers/update/<int:fundraiser_id>', views.update_fundraiser, name='update_fundraiser'),
    path('projects/', views.projects, name='projects'),  # View projects
    path('admin/', admin.site.urls),  # Admin panel
]
