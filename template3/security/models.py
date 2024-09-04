from django.db import models

# Create your models here.
class Candidate(models.Model):
    #define your table columns
    name = models.CharField(max_length=64)
    email = models.EmailField()
    Age = models.IntegerField()
    phone = models.IntegerField()
    country = models.CharField(max_length=64)


class Pastcandidate(models.Model):
    #define your table columns
    name = models.CharField(max_length=64)
    email = models.EmailField()
    Age = models.IntegerField()
    phone = models.IntegerField()
    country = models.CharField(max_length=64)