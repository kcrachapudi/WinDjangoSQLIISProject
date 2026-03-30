from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list),
    path('create/', views.create_request),
]