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
  path('categories/', views.CategoryList.as_view(), name='categories_index'),
  path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='categories_detail'),
  path('categories/create/', views.CategoryCreate.as_view(), name='categories_create'),
  path('categories/<int:pk>/update/', views.ToyUpdate.as_view(), name='categories_update'),
  path('categories/<int:pk>/delete/', views.ToyDelete.as_view(), name='categories_delete'),
]