from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Borrower)   
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number']    
admin.site.register(Business)
admin.site.register(Loan)
