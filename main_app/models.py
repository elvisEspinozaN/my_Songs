from django.db import models
from django.urls import reverse

TIMES = (
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

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    # a reverese look up
    # redirect created obj to the show page
    return reverse('detail', kwargs={'song_id': self.id})

class Play(models.Model):
  p_date = models.DateField()
  time = models.CharField(max_length=1, choices=TIMES, default=TIMES[2][1])
  # common connection through foreign key
  # CASCADE -> all related instances deleted those w/relation
  song = models.ForeignKey(Song, on_delete=models.CASCADE)

  def __str__(self):
    # get_< attr name >_display() is available due to attr = choices
    return f"{self.get_time_display()} on {self.p_date}"