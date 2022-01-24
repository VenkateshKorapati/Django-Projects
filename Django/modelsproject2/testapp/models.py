from django.db import models


# Create your models here.
class Job(models.Model):
    #Employee_name=models.CharField(max_length=64)
    Posting_date=models.CharField(max_length=64)
    Location=models.CharField(max_length=64)
    Offered_salary=models.FloatField()
    Qualification=models.CharField(max_length=64)
