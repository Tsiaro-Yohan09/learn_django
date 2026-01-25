from django.db import models

class Employee(models.Model):
    name = models.TextField()
    first_name = models.TextField()
    email = models.EmailField(unique=True, max_length=191)
    phone = models.TextField()
    poste = models.TextField()
    departement = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_embauche = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)