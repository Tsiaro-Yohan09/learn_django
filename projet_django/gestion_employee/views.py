from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Employee, Plannings

def create_employee(request):
    if request.method == "POST":
        name = request.POST["name"]
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        poste = request.POST["poste"]
        departement = request.POST["departement"]
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
            departement=departement,
            salary=salary,
            date_embauche=date_embauche
        )
        new_employee.save()
        
        return redirect("/liste_employer")
    
    return render(request, "create_employee.html")

def list_employee(request):
    list_employee = Employee.objects.all().values()
    
    template = loader.get_template("liste_employee.html")
    
    context = {
        "employees": list_employee,
    }
    
    return HttpResponse(template.render(context, request))

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
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        
        plannings = Plannings(
            date_work=date_work,
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