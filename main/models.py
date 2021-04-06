from django.db import models

# Create your models here.

class Patients(models.Model):
    name = models.CharField(max_length=50,null=False)
    dob= models.DateField(null=False)
    email=models.EmailField(unique=True,null=False)
    phone=models.CharField(max_length=10,unique=True,null=False)