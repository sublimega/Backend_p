# forms
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'username',
            'first_name',
            'last_name',
            'status',
            'student_type',
           
        ]
