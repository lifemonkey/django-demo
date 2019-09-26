from django import forms
from myapp.models import Student


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label="First name", max_length=50)
    last_name = forms.CharField(label="Last name", max_length=50)
    contact = forms.IntegerField(label="Phone number", min_value=0000000000, max_value=9999999999)
    email = forms.EmailField(label="Email", max_length=100)
    age = forms.IntegerField(label="Age", min_value=18, max_value=60)
    file = forms.FileField()

    class Meta:
        model = Student
        fields = "__all__"
