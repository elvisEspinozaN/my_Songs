from django.forms import ModelForm
from .models import Playback

class PlaybackForm(ModelForm):
  # Meta - class that creates classes
  class Meta:
    model = Playback
    fields = ('time', 'play')