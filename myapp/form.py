from django import forms
from myapp.models import Student
from myapp.models import Employee


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label="First name", max_length=50)
    last_name = forms.CharField(label="Last name", max_length=50)
    contact = forms.IntegerField
    email = forms.EmailField(label="Email", max_length=100)
    age = forms.IntegerField
    file = forms.FileField

    class Meta:
        model = Student
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
