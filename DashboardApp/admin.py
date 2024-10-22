from django.contrib import admin

# Register your models here.
from .models import Student,Program,Student_Profile,CohortGroup

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','last_name','status','student_type']




@admin.register(Student_Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['student','date_of_birth', 'rating','date_join','address']


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin) :
    list_display = ['courses','grade','student']


@admin.register(CohortGroup)
class CohortAdmin(admin.ModelAdmin) :
    list_display = ['name', 'date_join']



# Register your models here.
# admin.site.register(Student)
# admin.site.register(Program)
# admin.site.register(Student_Profile)
# admin.site.register(CohortGroup)






