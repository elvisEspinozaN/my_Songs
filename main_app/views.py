# renders to the dom or renders ourtemplates
from django.shortcuts import render, redirect
# this is just http responses into dom
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Song, Category, Photo
from .forms import PlaybackForm

import boto3
import uuid

S3_BASE_URL= 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'mysongs-eecn'

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

def delete_assoc_category(request, song_id, category_id):
  Song.objects.get(id=song_id).categories.remove(category_id)
  return redirect('detail', song_id=song_id)

def add_photo(request, song_id):
  # collect photo info - form submission
  """
    <input type='file' name='photo-file' />
  """
  photo_file = request.FILES.get('photo-file', None)
  # if statement to see if photo info is present
  if photo_file:
    # if photo present
    s3 = boto3.client('s3')
    # init ref to s3 service from boto3
    """
      random_img.png => abcc6a.png
    """
    # unique name for photo asset
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # attempt to upload to aws s3
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # save secure url to aws s3 hosted photo asset to db
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, song_id=song_id)
      photo.save()
      # if upload unsuccesful
    except Exception as error:
      print('***************************************')
      print('An error occurred while uploading to S3')
      print(error)
      print('***************************************')
      # print err to console
  # return a response as a redirect ot the client - redirecting to detail page
  return redirect('detail', song_id=song_id)

class SongCreate(CreateView):
  model = Song
  fields = ('name', 'genre', 'artist', 'date') # this provides all of the fields available

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