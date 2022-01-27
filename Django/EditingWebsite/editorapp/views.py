from django.shortcuts import render
from editorapp.models import *
# Create your views here.
def Index(request):
    return render(request,'editorapp/Index.html')

def Film_Edit_view(request):
    FilmEdit= FilmEditing.objects.all()
    return render(request,'editorapp/filmeditor.html',{'FilmEdit':FilmEdit})

def Wedding_Edit_view(request):
    WeddingEdit= WeddingEditing.objects.all()
    return render(request,'editorapp/weddingeditor.html',{'WeddingEdit':WeddingEdit})

def Birthaday_Edit_view(request):
    BirthdayEdit= BirthdayEditing.objects.all()
    return render(request,'editorapp/birthdayeditor.html',{'BirthdayEdit':BirthdayEdit})

def Business_Edit_view(request):
    BusinessEdit= BusinessEditing.objects.all()
    return render(request,'editorapp/businesseditor.html',{'BusinessEdit':BusinessEdit})

def Other_Edit_view(request):
   OtherEdit= OtherEditing.objects.all()
   return render(request,'editorapp/othereditor.html',{'OtherEdit':OtherEdit})



