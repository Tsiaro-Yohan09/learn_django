from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import (DemandeConger, Employee, Plannings,
                     Departement, Salary, TypeConge)

def create_employee(request):
    departement = Departement.objects.all().values()
    if request.method == "POST":
        name = request.POST["name"]
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        poste = request.POST["poste"]
        departement_id = request.POST["departement"]
        salary = request.POST["salary"]
        date_embauche = request.POST["date_embauche"]
        
        is_exist = Employee.objects.filter(email=email).exists()

        if is_exist:
            return render(request, 'create_employee.html', {
                'error_message': "Cet email est déjà utilisé par un autre employé.",
                'data_saisie': request.POST
            })
        
        new_employee = Employee(
            name=name,
            first_name=first_name,
            email=email,
            phone=phone,
            poste=poste,
            departement_id=departement_id,
            salary=salary,
            date_embauche=date_embauche
        )
        new_employee.save()
        
        return redirect("/liste_employer")
    
    return render(request, "create_employee.html", {"departement": departement})

def list_employee(request):
    list_employee = Employee.objects.select_related('departement').all()
    
    context = {
        "employees": list_employee,
    }
    
    return render(request, "liste_employee.html", {"employees": list_employee})

def information_employee(request, id):
    employee = Employee.objects.get(id=id)
    
    return render(request, "informations.html", {"employee": employee})

def edit_employee(request, id):
    if id:
        get_employee = Employee.objects.get(id=id)
        if request.method == "POST":
            get_employee.name = request.POST["name"]
            get_employee.first_name = request.POST["first_name"]
            get_employee.email = request.POST["email"]
            get_employee.phone = request.POST["phone"]
            get_employee.poste = request.POST["poste"]
            get_employee.departement = request.POST["departement"]
            get_employee.salary = request.POST["salary"]
            get_employee.date_embauche = request.POST["date_embauche"]
            
            get_employee.save()
            return redirect("/liste_employer")
                
        # get_employee = Employee.objects.get(id=id)
        return render(request, "edit_employee.html", {"employee": get_employee})
    else:
        return HttpResponse("Id not found ou Employer")
    
def delete_employee(request, id):
    get_employee = Employee.objects.get(id=id)
    if request.method == "POST":
        get_employee.delete()
        return redirect("/liste_employer")
    
    return render(request, "confirmation_delete.html", {"employee": get_employee})
    
def create_plannings(request):
    employee = Employee.objects.all().values()
    
    if request.method == "POST":
        date_work = request.POST["date_work"]
        status = request.POST["status"]
        employee_id_id = request.POST["employee_id"]
        heure_retard = request.POST["heure_retard"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        
        plannings = Plannings(
            date_work=date_work,
            heure_retard=heure_retard,
            start_time=start_time,
            end_time=end_time,
            status=status,
            employee_id_id=employee_id_id
        )
        plannings.save()
        
        return redirect("/liste_employer")
    
    return render(request, 'create_plannings.html', {"employee": employee})

def liste_plannings(request): 
    plannings = Plannings.objects.select_related('employee_id').all()
    
    return render(request, "liste_plannings.html", {"plannings": plannings})

def add_departement(request):
    if request.method == "POST":
        name_departement = request.POST["departement"]
        
        new_depart = Departement(
            name_departement=name_departement
        )
        new_depart.save()
        
        # return redirect("/liste_employer")
    
    
    return render(request, "departement/add_departement.html")
    
def list_departement(request):
    departement = Departement.objects.all().values()
    
    return render(request, "departement/list_departement.html", {"departement": departement})

def paye_salary(request, id):
    if request.method == "POST":
        month = request.POST["month"]
        year = request.POST["year"]
        primes = request.POST["primes"]
        deduction = request.POST["deduction"]
        salary_net = request.POST["salary_net"]
        
        salary = Salary(
            employee_id = id,
            month=month,
            year=year,
            primes=primes,
            deduction=deduction,
            salary_net=salary_net
        )
        salary.save()
    return render(request, "salaire/paye_salary.html")

def list_salary(request):
    salary = Salary.objects.select_related('employee').all()
    
    return render(request, "salaire/liste_salary.html", {"salary": salary})

def types_conger(request):
    if request.method == "POST":
        name_conge = request.POST["name_conge"]
        isPaye = request.POST["isPaye"]
        justification = request.POST["justification"]
        
        type_conge = TypeConge(
            name_conge=name_conge,
            isPaye=isPaye,
            justification=justification
        )
        type_conge.save()
        
        return redirect("/liste_employer")
    
    return render(request, "conges/types_conges.html")

def demande_conges(request, id):
    types_conger = TypeConge.objects.all().values()
    
    if request.method == "POST":
        typeconge = request.POST["typeconge"]
        date_debut = request.POST["date_debut"]
        date_fin = request.POST["date_fin"]
        status = request.POST["status"]
        
        date_debut = datetime.strptime(date_debut, '%Y-%m-%d').date()
        date_fin = datetime.strptime(date_fin, '%Y-%m-%d').date()

        total_day = date_fin - date_debut
        
        
        new_conge = DemandeConger(
            date_debut=date_debut,
            date_fin=date_fin,
            total_day=total_day.days,
            status=status,
            employee_id=id,
            typeconge_id=typeconge
        )
        new_conge.save()
        # return redirect("")
        
    return render(request, "conges/demande_conges.html", {"typeconge": types_conger})

def liste_conges(request):
    demande_conges = DemandeConger.objects.select_related("employee", "typeconge").all()
    
    return render(request, "conges/liste_conges.html", {"demande_conges": demande_conges})
