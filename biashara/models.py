from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Borrower(models.Model):
    name = models.CharField(max_length=50 ,null=True, blank=True)
    email = models.EmailField(max_length=255, unique =True)
    phone_number = models.CharField(max_length=10,unique=True,blank=True) 
    
    
    def save_user(self):
            self.save()
        
    def delete_user(self):
        self.save()   
        
    def __str__(self):
        return f"{self.name}"
    


business_sector_choices=(
    ('retail', 'retail'),
    ('professional services', 'professional services'),
    ('food and drinks', 'food and drinks'),
    ('entertainment', 'entertainment'),
    
)

class Business(models.Model):
        business_name = models.CharField(max_length=50 ,null=True, blank=True)
        business_address = models.CharField(max_length=15 ,null=True, blank=True)
        description = models.TextField(max_length=250, blank=True)
        company_number = models.PositiveIntegerField(max_length=8 ,null=True, blank=True,unique=True ,validators=[RegexValidator(r'^\d{1,10}$')])
        business_sector = models.CharField(max_length=100, choices=business_sector_choices)
        
        def save_business(self):
            self.save()
     
        def delete_business(self):
             self.delete()
             
        def __str__(self):
            return self.business_name
class Loan(models.Model):
       amount = models.IntegerField(validators=[MaxValueValidator(100000),MinValueValidator(10000)])
       reason = models.TextField(max_length=250, blank=True)
       days = models.IntegerField(max_length=250, blank=True)
       borrower =models.ForeignKey(Borrower, on_delete=models.CASCADE)
       business =models.ForeignKey(Business, on_delete=models.CASCADE)
       
       
       def __str__(self):
            return self.reason 
             
             
             

        
    
    
    
    
    