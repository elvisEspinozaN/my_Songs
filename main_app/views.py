from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('HelloWorld')

def about(request):
  return HttpResponse('about page')