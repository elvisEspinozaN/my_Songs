from django.contrib import admin
from .models import Song, Category, Playback, Photo

# Register your models here.

admin.site.register(Song)
admin.site.register(Category)
admin.site.register(Playback)
admin.site.register(Photo)
