from tkinter import CASCADE
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
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.TextField()
    
class Departement(models.Model):
    name_departement = models.TextField()