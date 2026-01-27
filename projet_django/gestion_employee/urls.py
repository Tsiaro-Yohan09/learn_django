from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employee, name='liste_employer'),
    path('creer_employer/', views.create_employee, name='creer_employee'),
    path('informations_employer/<int:id>', views.information_employee, name='informations_employer'),
    path('informations_employer/editer_employer/<int:id>', views.edit_employee, name='editer_employer'),
    path('informations_employer/supprimer_employer/<int:id>', views.delete_employee, name='supprimer_employer'),
    path('gerer_presence/', views.create_plannings, name='gerer_presence'),
    path('liste_presence/', views.liste_plannings, name='liste_presence'),
    path('ajouter_departement/', views.add_departement, name='ajouter_departement'),
]