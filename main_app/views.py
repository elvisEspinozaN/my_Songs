# renders to the dom or renders ourtemplates
from django.shortcuts import render
# this is just http responses into dom
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def songs_index(request):
  return render(request, 'songs/index.html', {'songs': songs})