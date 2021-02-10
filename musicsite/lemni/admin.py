from django.contrib import admin
from .models import Genre, Artist, Clip, Song, MyUser

admin.site.register(MyUser)

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['name', 'slug']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Genre, GenreAdmin)


class ClipAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    list_display_links = ['title']
    search_fields = ['title']


admin.site.register(Clip, ClipAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'cover', 'release_date', 'description', 'lyrics']
    list_display_links = ['name']
    search_fields = ['name', 'artist', 'feature']
    prepopulated_fields = {'slug': ('artist', 'name')}


admin.site.register(Song, SongAdmin)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['alias', 'slug', 'first_name', 'last_name', 'birthday', 'photo', 'description']
    list_display_links = ['alias']
    search_fields = ['alias', 'first_name', 'slug']
    prepopulated_fields = {'slug': ('alias',)}


admin.site.register(Artist, ArtistAdmin)
