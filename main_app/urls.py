# generates url paths
from django.urls import path
# enitre functionality from views.py
from . import views

# GET /songs/1
# python doesn't allow type coercion - <int: xxx> allows it to look 
# at the str as an int

# this variable is always needed
urlpatterns = [
  # home page
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('songs/', views.songs_index, name='index'),
  path('songs/<int:song_id>/', views.songs_detail, name='detail'),
]