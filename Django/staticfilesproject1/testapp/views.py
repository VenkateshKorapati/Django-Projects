from django.shortcuts import render
import datetime
# Create your views here.
def date_time_view(request):
    date = datetime.datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        msg='Hello Darling Very Good Morning!!!'
    elif h<16:
        msg='Hello Darling Very Good AfterNoon!!!'
    elif h<21:
        msg='Hello Darling Very Good Evening!!!'
    else:
        msg='Hello Darling Very Good Night!!!'
    my_dict={'date':date,'msg':msg}

    return render(request,'testapp/results.html',my_dict)
