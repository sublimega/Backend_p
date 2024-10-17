from django import forms
from .models import Student

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'first_name','last_name', 'status', 'student_type']
        # fields = ['profile_image', 'full_name', 'cohort', 'program', 'status', 'date_joined', 'rating']
