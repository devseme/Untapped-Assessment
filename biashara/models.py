from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50 ,null=True, blank=True)
    email = models.EmailField(max_length=255, unique =True)
    phone_number = models.CharField(max_length=10,unique=True,blank=True) 
    
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.save()   
        
    def __str__(self):
        return self.user.username   
class Business_sector(models.Model):
    description =models.TextField 
    
    def __str__(self):
         return self.description 
class Amount(models.Model):
       amount = models.DecimalField(max_digits=6, decimal_places=2)
       reason = models.TextField(max_length=250, blank=True)
       
       
       def __str__(self):
            return self.reason      

class Business(models.Model):
        business_name = models.CharField(max_length=50 ,null=True, blank=True)
        business_address = models.CharField(max_length=15 ,null=True, blank=True)
        description = models.TextField(max_length=250, blank=True)
        company_number = models.PositiveIntegerField(max_length=8 ,null=True, blank=True,unique=True ,validators=[RegexValidator(r'^\d{1,10}$')])
        Business_sector = models.ManyToManyField(Business_sector, related_name='business_sector')
        def save_business(self):
            self.save()
     
        def delete_business(self):
             self.delete()
             
        def __str__(self):
            return self.description     

             
             

        
    
    
    
    
    