# renders to the dom or renders ourtemplates
from django.shortcuts import render
# this is just http responses into dom
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('HelloWorld')

def about(request):
  return render(request, 'about.html')