from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Student
from .forms import UserProfileForm

# Create your views here.

class HompageView(View):
    def get(self, request):
        form = UserProfileForm()
        users = Student.objects.all()
        return render(request, 'indexmain.html', {'form': form, 'users': users})

    def post(self, request):
       form = UserProfileForm(request.POST)
    #    if request.method == 'POST':
       if form.is_valid():
             form.save()
             users = Student.objects.all()  # Get updated user list
             return render(request, 'indexmain.html', { 'users': users})
        #    return redirect('homeview')  
       else:
        #  form = UserProfileForm()
    
          users = Student.objects.all()
          return render(request, 'indexmain.html', {'form': form, 'users': users})
    
    

    
    # def about(self, request):
    #     return render(request, 'about.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')