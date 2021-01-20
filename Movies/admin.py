from django.contrib import admin
from . models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'genre')

admin.site.register(Movie, MovieAdmin)