import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','vjobsproject.settings')
django.setup()
from jobapp.models import *
from faker import Faker
from random import *
fake=Faker()

def phnumbergen():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('TEAM LEAD','PROJECT LEAD','SOFTWARE ENGINEER'))
        feligibility=fake.random_element(elements=('Btech','Mtech','MCA'))
        faddress=fake.address()
        femail=fake.email()
        fphnumber=phnumbergen()
        HYDjob_record=HydJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphnumber)
        BLRjob_record=BlrJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphnumber)
        CHENNAIjob_record=ChennaiJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphnumber)
        PUNE_record=PuneJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphnumber)

populate(30)
