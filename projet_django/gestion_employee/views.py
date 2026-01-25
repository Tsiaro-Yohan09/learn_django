from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Employee

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