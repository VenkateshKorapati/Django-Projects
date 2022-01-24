from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField()
    ph_number=models.IntegerField()
    address=models.TextField()