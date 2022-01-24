from django.shortcuts import render
from testapp.models import Job
# Create your views here.
def Job_info_view(request):
    Job_details = Job.objects.all()
    return render(request,'testapp/results.html',{'Job_details':Job_details})
