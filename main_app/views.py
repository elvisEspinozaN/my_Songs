# renders to the dom or renders ourtemplates
from django.shortcuts import render, redirect
# this is just http responses into dom
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Song, Category
from .forms import PlaybackForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def songs_index(request):
  songs = Song.objects.all()
  return render(request, 'songs/index.html', {'songs': songs})

def songs_detail(request, song_id):
  song = Song.objects.get(id=song_id)
  playback_form = PlaybackForm()
  
  # looking up field lookup => 'id'
  # we're getting eveything thst doesn't belong to this song
  categories_song_doesnt_have = Category.objects.exclude(id__in = song.categories.all().values_list('id'))

  return render(request, 'songs/detail.html', {
    'song': song,
    'playback_form': playback_form,
    'categories': categories_song_doesnt_have
  })

def add_playback(request, song_id):
  # collect form inp vals
  form = PlaybackForm(request.POST)
  # valid inp vals
  if form.is_valid():
    # save copy of new playback inst
    new_playback = form.save(commit=False)
    # attach a ref to obj that owns playback
    new_playback.song_id = song_id
    # save playback to db
    new_playback.save()
  # redirect to details pg
  return redirect('detail', song_id=song_id)

def assoc_category(request, song_id, category_id):
  Song.objects.get(id=song_id).categories.add(category_id)
  return redirect('detail', song_id=song_id)

class SongCreate(CreateView):
  model = Song
  fields = '__all__' # this provides all of the fields available

class SongUpdate(UpdateView):
  model = Song
  fields = ('name', 'genre', 'artist', 'date')

class SongDelete(DeleteView):
  model = Song
  success_url = '/songs/'

class CategoryCreate(CreateView):
  model = Category
  fields = ('name', 'color')

class CategoryUpdate(UpdateView):
  model = Category
  fields = ('name', 'color')

class CategoryDelete(DeleteView):
  model = Category
  success_url = '/categories/'

class CategoryDetail(DetailView):
  model = Category
  template_name = 'categories/detail.html'

class CategoryList(ListView):
  model = Category
  template_name = 'categories/index.html'