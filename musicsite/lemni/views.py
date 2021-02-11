from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View, TemplateView

from .forms import LoginForm, RegistrationForm
from .models import Artist, Genre, Song, Clip, MyUser


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
        artist = get_object_or_404(Artist, id=id, slug=slug)
        context = {'artist': artist}
        return render (request, 'lemni/artist_detail.html', context)


class SongsView(View):
    def get(self, request):
        songs = Song.objects.all()
        context = {'songs': songs}
        return render(request, 'lemni/songs_list.html', context)


class SongDetail(View):
    def get(self, request, slug):
        song= get_object_or_404(Song, slug=slug)
        context = {'song': song}
        return render(request, 'lemni/song_detail.html', context)


class ArtistSongsView(View):
    def get(self, request, artist_slug):
        # if id:
        #     songs = Song.objects.filter(artist=id)
        # else:
        #     songs = Song.objects.all()
        artist = None
        # songs = Song.objects.filter(artist_slug=artist_slug)
        songs = Song.objects.filter(artist__alias='A$AP Rocky')

        # songs = get_object_or_404(Song) Pay attention to it!!!


        # songs = Song.objects.all()
                # if artist_slug:
        #     artist = get_object_or_404(Artist, slug=artist_slug)
        #     songs = Song.objects.filter(artist=artist.id)
        #     # print('HIIIII')
        context = {'songs': songs}
        return render(request, 'lemni/songs_list.html', context)

class ClipsView(View):
    def get(self, request):
        clips = Clip.objects.all()
        context = {'clips': clips}
        return render(request, 'lemni/clips_list.html', context)

class LemniLoginView(LoginView):
    template_name = 'user/login.html'
    # redirect_field_name = ''
    authentication_form = LoginForm


@login_required
def profile(request):
    return render(request, 'user/profile.html')


class RegistrationUserView(CreateView):
    model = MyUser
    template_name = 'user/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user/registration_done.html')


class RegistrationDoneView(TemplateView):
    template_name = 'user/registration_done.html'

