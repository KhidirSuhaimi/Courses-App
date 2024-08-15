from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length= 30)
    description =  models.CharField(max_length= 140)
    instructor = models.CharField( max_length=50)
    rating  =models.FloatField()
    