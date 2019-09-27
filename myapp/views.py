from django.shortcuts import render, redirect
# import loading from django template
from django.http import HttpResponse
# import class
from myapp.functions.functions import handle_uploaded_file
from myapp.form import StudentForm, EmployeeForm
from myapp.models import Employee


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_student(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
    else:
        student = StudentForm()
        return render(request, 'add_student.html', {'form': student})


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form':form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance= employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
