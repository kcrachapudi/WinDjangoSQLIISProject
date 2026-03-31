from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('create/', views.request_create, name='request_create'),
    path('edit/<int:pk>/', views.request_edit, name='request_edit'),
    path('delete/<int:pk>/', views.request_delete, name='request_delete'),
]