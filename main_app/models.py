from django.db import models
from django.urls import reverse

# Create your models here.
class Song(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  artist = models.CharField(max_length=100)
  date = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    # a reverese look up
    # redirect created obj to the show page
    return reverse('detail', kwargs={'song_id': self.id})