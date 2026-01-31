from pyexpat import model
from tkinter import CASCADE
from turtle import mode
from django.db import models

class Employee(models.Model):
    name = models.TextField()
    first_name = models.TextField()
    email = models.EmailField(unique=True, max_length=191)
    phone = models.TextField()
    poste = models.TextField()
    departement = models.ForeignKey("Departement", on_delete=models.CASCADE, related_name='employes')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_embauche = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    
class Plannings(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='horaires')
    date_work = models.DateField()
    heure_retard = models.TimeField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.TextField()
    
class Departement(models.Model):
    name_departement = models.TextField()
    
class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="salary_history")
    month = models.TextField()
    year = models.TextField()
    primes = models.TextField()
    deduction = models.TextField()
    salary_net = models.FloatField()
    
class TypeConge(models.Model):
    name_conge = models.TextField()
    isPaye = models.TextField()
    justification = models.TextField()
    
class DemandeConger(models.Model):
    typeconge = models.ForeignKey(TypeConge, on_delete=models.CASCADE, related_name="conges")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="demande_conges")
    date_debut = models.DateField()
    date_fin = models.DateField()
    total_day = models.IntegerField()
    status = models.TextField()