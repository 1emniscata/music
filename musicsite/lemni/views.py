from django.shortcuts import render
from django.views.generic.base import View
from .models import Artist, Genre, Song, Clip


def main(request):
    return render(request, 'lemni/base.html')


class ArtistsView(View):
    def get(self, request):
        artists = Artist.objects.all()
        context = {'artists': artists}
        return render(request, 'lemni/artists_list.html', context)


class ArtistDetail(View):
    def get(self, request, id, slug):
        # artist = Artist.objects.all() # filter by slug
        artist = get_object_or_404()
        context = {'artist': artist}
        return render (request, 'lemni/artist_detail.html', context)


class SongsView(View):
    def get(self, request):
        songs = Song.objects.all()
        context = {'songs': songs}
        return render(request, 'lemni/songs_list.html', context)


class ClipsView(View):
    def get(self, request):
        clips = Clip.objects.all()
        context = {'clips': clips}
        return render(request, 'lemni/clips_list.html', context)



