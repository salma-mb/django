from django.db import models

# Create your models here.
class Candidate(models.Model):
    #define your table columns
    fullname = models.CharField(max_length=64)
    email = models.EmailField()
    password= models.CharField(max_length=64)
    phone = models.IntegerField()
    country = models.CharField(max_length=64)
    address = models.CharField(max_length=64)