from django.contrib import admin
from .models import Song, Category

# Register your models here.

admin.site.register(Song)
admin.site.register(Category)