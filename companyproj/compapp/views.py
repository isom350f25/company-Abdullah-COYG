from django.shortcuts import render
from .models import Employee

def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

# Create your views here.
