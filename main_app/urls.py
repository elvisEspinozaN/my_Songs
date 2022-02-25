# generates url paths
from django.urls import path
# enitre functionality from views.py
from . import views

# this variable is always needed
urlpatterns = [
  # home page
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
]