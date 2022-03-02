from pyexpat import model
from django.db import models

# Create your models here.

class Mobile(models.Model):
    Brand = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Price = models.IntegerField()
    Description = models.TextField()