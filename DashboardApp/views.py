from django.shortcuts import render
from django.views.generic import View
from .models import Student

# Create your views here.
class HompageView(View):
    def get(self, request):
        students = Student.objects.all() # Getting all the student data to display
        return render(request, 'indexmain.html', {'students': students})
    
    # def about(self, request):
    #     return render(request, 'about.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
