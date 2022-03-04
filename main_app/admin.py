from django.contrib import admin
from .models import Song, Category, Playback

# Register your models here.

admin.site.register(Song)
admin.site.register(Category)
admin.site.register(Playback)