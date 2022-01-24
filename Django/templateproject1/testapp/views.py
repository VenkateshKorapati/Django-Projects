from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def template_view(request):
    dt=datetime.datetime.now()

    name='venky'
    mobileno=8500646952
    address='Bendapudi'
    my_dict={'date':dt,'name':name,'mobileno':mobileno,'address':address}
    return render(request,'testapp/results.html',my_dict)
