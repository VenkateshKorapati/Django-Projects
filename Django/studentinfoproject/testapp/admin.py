from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['roll_no','name','dob','email','ph_number','address']
admin.site.register(Student,StudentAdmin)