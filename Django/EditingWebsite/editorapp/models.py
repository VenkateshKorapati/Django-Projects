from django.db import models

# Create your models here.
class FilmEditing(models.Model):
    ShortFilms=models.CharField(max_length=64)
    Documentaries=models.CharField(max_length=64)
    MusicAlbums=models.CharField(max_length=64)
    FeatureFilms=models.CharField(max_length=64)
    AdFilms=models.CharField(max_length=64)

class WeddingEditing(models.Model):
    PreWedding=models.CharField(max_length=64)
    PostWedding=models.CharField(max_length=64)
    Bride_Bridegroom=models.CharField(max_length=64)
    Haldi=models.CharField(max_length=64)
    Mehandi=models.CharField(max_length=64)
    FinalWedding=models.CharField(max_length=64)

class BirthdayEditing(models.Model): 
    FirstBirthday=models.CharField(max_length=64)
    MonthlyBirthday=models.CharField(max_length=64)

class BusinessEditing(models.Model): 
    CompanyProfile=models.CharField(max_length=64)
    ProductReview=models.CharField(max_length=64)

class OtherEditing(models.Model): 
    MatureFuntions=models.CharField(max_length=64)
    PregnantSpecial=models.CharField(max_length=64)
    Retirement=models.CharField(max_length=64)