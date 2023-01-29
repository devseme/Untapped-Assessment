from rest_framework import serializers
from .models import *

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'
        
class LoanSerializer(serializers.ModelSerializer):
    borrower_name = serializers.CharField(source='borrower.name')
    business_name = serializers.CharField(source='business.business_name')
    class Meta:
        model = Loan
        fields = ['amount','days','reason','borrower_name','business_name']  
        
class BusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = '__all__'              
        
        
       