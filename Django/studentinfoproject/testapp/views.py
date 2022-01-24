from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def student_info_view(request):
    info=Student.objects.all()
    # info=Student.objects.filter(name__startswith='M')

    return render(request,'testapp/info.html',{'info':info})