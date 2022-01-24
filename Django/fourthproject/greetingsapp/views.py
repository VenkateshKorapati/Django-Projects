from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greetings_view(request):
    return HttpResponse('<h1>Hello My Dear Have a great day</h1>')
