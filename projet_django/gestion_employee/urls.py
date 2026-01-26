from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employee, name='liste_employer'),
    path('creer_employer/', views.create_employee, name='creer_employee'),
    path('informations_employer/<int:id>', views.information_employee, name='informations_employer'),
    path('informations_employer/editer_employer/<int:id>', views.edit_employee, name='editer_employer'),
    path('informations_employer/supprimer_employer/<int:id>', views.delete_employee, name='supprimer_employer'),
]