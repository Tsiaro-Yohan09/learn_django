from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_employee, name='employee'),
    path('liste/', views.list_employee, name='liste')
]