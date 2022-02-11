from .models import Video
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        # fields = ['title', 'url', 'youtube_id']
        fields = ['url']
        labels = {'url':'YouTube_url'}
class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label="search for videos")