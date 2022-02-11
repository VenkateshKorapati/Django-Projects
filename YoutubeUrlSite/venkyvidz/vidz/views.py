from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Vidzs,Video
from .forms import VideoForm,SearchForm

YOUTUBE_API_KEY = 'AIzaSyBuM7q9U1f-O6t4Gyg4zsxstDiEHRxbWYQ'

# Create your views here.
def home(request):
    context = {}
    return render(request,'vidz/home.html',context)

def dashboard(request):
    context = {}
    return render(request,'vidz/dashboard.html',context)

def add_video(request, pk):
    form = VideoForm()
    search_form = SearchForm()

    if request.method == "POST":
        filled_form = VideoForm(request.POST)
        if filled_form.is_valid():
            video = Video()
            video.url = filled_form.cleaned_data['url']
            video.title = filled_form.cleaned_data['title']
            video.youtube_id = filled_form.cleaned_data['youtube_id']
            video.vidzs = Vidzs.objects.get(pk=pk)
            video.save()

    return render(request, 'vidz/add_video.html',{'form':form,'search_form':search_form})


class  SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view=super(SignUp,self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')        
        user = authenticate(username=username,password=password)
        login(self.request,user)
        return view

class CreateVidz(generic.CreateView):
    model = Vidzs
    fields = ['title']
    template_name = 'vidz/create_vidz.html' 
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateVidz,self).form_valid(form)
        return redirect('home')

class DetailVidz(generic.DetailView):
    model = Vidzs
    template_name = 'vidz/detail_vidz.html'

class UpdateVidz(generic.UpdateView):
    model = Vidzs
    template_name = 'vidz/update_vidz.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')
    
class DeleteVidz(generic.DeleteView):
    model = Vidzs
    template_name = 'vidz/delete_vidz.html'
    success_url = reverse_lazy('dashboard')
