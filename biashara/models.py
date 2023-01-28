from django.db import models

# Create your models here.
class Borrower(models.Model):
    name = models.CharField(max_length=50 ,null=True, blank=True)
    email = models.EmailField(max_length=255, unique =True)
    phone_number = models.CharField(max_length=10,unique=True,blank=True) 