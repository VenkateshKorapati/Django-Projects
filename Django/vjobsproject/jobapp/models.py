from email.headerregistry import Address
from django.db import models

# Create your models here.
class Job(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=64)
    eligibility=models.CharField(max_length=32)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.IntegerField()

class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=64)
    eligibility=models.CharField(max_length=32)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.IntegerField()

class BlrJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=64)
    eligibility=models.CharField(max_length=32)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.IntegerField()

class ChennaiJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=64)
    eligibility=models.CharField(max_length=32)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.IntegerField()

class PuneJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=64)
    eligibility=models.CharField(max_length=32)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.IntegerField()