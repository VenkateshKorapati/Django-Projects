from django.shortcuts import render
import datetime

# Create your views here.
def wishes_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='Hi Darlings very good '
    if h<12:
        msg=msg+'Morning'
    elif h<16:
        msg=msg+'afternoon'
    elif h<21:
        msg=msg+'Evening'
    else:
        msg=msg+'Night'
    return render(request,'testapp/results.html',{'msg':msg,'date':date})
