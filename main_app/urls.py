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
  path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
  # has to take in pk - cos of db lookup
  path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
  path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
]