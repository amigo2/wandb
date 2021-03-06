
from django.contrib import admin
from django.urls import path, include 
from crudapp import views
from .views import Home 

urlpatterns = [
    path("", Home.as_view(), name='home'),
    #path('contacts/', views.IndexView.as_view(), name='index'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    path('contacts/edit/<int:pk>/', views.edit, name='edit'),
    path('contacts/create/', views.create, name='create'),
    path('contacts/delete/<int:pk>/', views.delete, name='delete'),
]