from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view(request):
    return HttpResponse('<h1>This response is from first view</h1>')
def second_view(request):
    return HttpResponse('<h1>This response is from second view</h1>')
def third_view(request):
    return HttpResponse('<h1>This response is from third view</h1>')
def fourth_view(request):
    return HttpResponse('<h1>This response is from fouth view</h1>')
def fifth_view(request):
    return HttpResponse('<h1>This response is from fifth view</h1>')
