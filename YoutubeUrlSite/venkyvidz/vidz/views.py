from urllib import response
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Vidzs,Video
from .forms import VideoForm,SearchForm
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
import urllib
import requests


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
    vidzs = Vidzs.objects.get(pk=pk)

    if not vidzs.user == request.user:
        raise Http404
    
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            video = Video()
            video.vidzs = vidzs
            video.url = form.cleaned_data['url']
            parsed_url = urllib.parse.urlparse(video.url)
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            if video_id:
                video.youtube_id = video_id[0]
                response = requests.get(f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={ video_id[0] }&key={YOUTUBE_API_KEY}')
                json = response.json()
                title = json['items'][0]['snippet']['title']     
                video.title = title
                video.save()
                return redirect('detail_vidz', pk)

            else:
                errors= form._errors.setdefault('url',ErrorList())
                errors.append('Needs to be a YouTube URL')


    context = {'form':form,'search_form':search_form,'vidzs':vidzs}        
    return render(request, 'vidz/add_video.html',context)

            

def video_search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        encoded_search_term = urllib.parse.quote(search_form.cleaned_data['search_term'])
        response = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&q={ encoded_search_term }&key={YOUTUBE_API_KEY}')    
        return JsonResponse(response.json())
    return JsonResponse({'error':'Not able to validate form'})

class DeleteVideo(generic.DeleteView):
    model = Video
    template_name = 'vidz/delete_video.html'
    success_url = reverse_lazy('dashboard')

    
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
