from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employee, name='liste_employer'),
    path('informations_employer/<int:id>', views.information_employee, name='informations_employer'),
    path('creer_employer/', views.create_employee, name='creer_employee'),
]