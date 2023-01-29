from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from.serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
# Create your views here.

   
@api_view(['GET'])
def get_all_borrowers(request):
    if request.method == "GET":
        borrower = Borrower.objects.all()
        serializer =BorrowerSerializer(borrower ,many =True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_borrowers_by_id(request ,borrower_id):
    if request.method == "GET":
        borrower =Borrower.objects.filter(id = borrower_id)
        serializer =BorrowerSerializer(borrower,many=True)
        return Response(serializer.data) 


@api_view(['GET'])
def get_all_business(request):
    if request.method == "GET":
        bus = Business.objects.all()
        serializer =BusinessSerializer(bus ,many =True)
        return Response(serializer.data)
@api_view(['GET'])
def get_business_by_id(request ,business_id):
    if request.method == "GET":
        business =Business.objects.filter(id= business_id)
        serializer =BusinessSerializer(business,many=True)
        return Response(serializer.data) 
    

@api_view(['GET'])
def get_all_loans(request):
    if request.method == "GET":
        loan = Loan.objects.all()
        serializer =LoanSerializer(loan ,many =True)
        return Response(serializer.data)
@api_view(['GET'])
def get_loan_by_id(request ,loan_id):
    if request.method == "GET":
        loan =Loan.objects.filter(id= loan_id)
        serializer =LoanSerializer(loan,many=True)
        return Response(serializer.data) 
    