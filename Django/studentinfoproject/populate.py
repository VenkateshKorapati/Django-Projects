import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentinfoproject.settings')
django.setup()
from testapp.models import *
from faker import Faker
from random import *
def phnumbergen():
    d1=randint(7,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    f=Faker()
    for i in range(n):
        frollno=f.random_int(min=1,max=500)
        fname=f.name()
        fdob=f.date()
        femail=f.email()
        fphnumber=phnumbergen()
        faddr=f.address()
        studentinfo_record=Student.objects.get_or_create(roll_no=frollno,name=fname,dob=fdob,email=femail,ph_number=fphnumber,address=faddr)
populate(30)