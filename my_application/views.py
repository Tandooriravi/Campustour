from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def home(request):
   return render(request,'common/home.html')

def campus(request):
   return render(request,'common/campus.html')

def sports(request):
   return render(request,'common/sports.html')

def teachers(request):
   return render(request,'common/teachers.html')
