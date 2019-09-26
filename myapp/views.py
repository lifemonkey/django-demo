from django.shortcuts import render
# import loading from django template
from django.http import HttpResponse
# import class
from myapp.form import StudentForm
from myapp.functions.functions import handle_uploaded_file


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

