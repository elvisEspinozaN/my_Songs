from django.db import models
from django.urls import reverse
from datetime import date

PLAYS = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('categories_detail', kwargs={'pk': self.id})

class Song(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  artist = models.CharField(max_length=100)
  date = models.IntegerField()
  categories = models.ManyToManyField(Category)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    # a reverese look up
    # redirect created obj to the show page
    return reverse('detail', kwargs={'song_id': self.id})

  def playback_for_today(self):
    return self.playback_set.filter(time=date.today()).count() >= len(PLAYS)

class Playback(models.Model):
  time = models.DateField('playback date')
  play = models.CharField(max_length=1, choices=PLAYS, default=PLAYS[0][0])
  # connection through FK
  # CASCADE deletes related to data
  song = models.ForeignKey(Song, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_play_display()} on {self.time}"

  class Meta:
    ordering = ('-time',)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  song = models.ForeignKey(Song, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for song_id: {self.song_id} @{self.url}"