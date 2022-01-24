from django.db import models

# Create your models here.
class Book(models.Model):
    Author=models.CharField(max_length=64)
    Book_no=models.IntegerField()
    Book_Title=models.CharField(max_length=64)
    Published_date=models.CharField(max_length=64)
