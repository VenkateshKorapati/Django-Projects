from django.shortcuts import render

# Create your views here.

def news_portal_view(request):
    portal='ALL KINDS OF NEWS AVAILABLE HERE'
    return render(request,'newsapp/display.html',{'portal':portal})
def political_news_view(request):
    news='Political Dhandaa'
    return render(request,'newsapp/politics.html',{'news':news})
def sports_news_view(request):
    news1='Sports Mania'
    return render(request,'newsapp/sports.html',{'news1':news1})
def movies_news_view(request):
    news2='Movies Adda'
    return render(request,'newsapp/movies.html',{'news2':news2})
