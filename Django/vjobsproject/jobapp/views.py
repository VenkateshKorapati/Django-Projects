from django.shortcuts import render
from jobapp.models import Job
from jobapp.models import HydJobs
from jobapp.models import BlrJobs
from jobapp.models import ChennaiJobs
from jobapp.models import PuneJobs
# Create your views here.
def job_info_view(request):
    jobinfo=Job.objects.all().order_by('date')
    return render(request,'jobapp/jobs.html',{'jobinfo':jobinfo})

def hyd_info_view(request):
    hydjob=HydJobs.objects.all().order_by('date')
    return render(request,'jobapp/jobsinhyd.html',{'hydjob':hydjob})

def blr_info_view(request):
    blrjob=BlrJobs.objects.all().order_by('-date')
    return render(request,'jobapp/jobsinblr.html',{'blrjob':blrjob})

def chennai_info_view(request):
    chennaijob=ChennaiJobs.objects.all().order_by('date')
    return render(request,'jobapp/jobsinchennai.html',{'chennaijob':chennaijob})

def pune_info_view(request):
    punejob=PuneJobs.objects.all().order_by('date')
    return render(request,'jobapp/jobsinpune.html',{'punejob':punejob})