from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.signing import BadSignature
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View, TemplateView

from .forms import LoginForm, RegistrationForm
from .models import Artist, Genre, Song, Clip, MyUser, Album
from .utilities import signer


def main(request):
    return render(request, 'lemni/base.html')


class ArtistsView(View):
    def get(self, request):
        artists = Artist.objects.all()
        context = {'artists': artists}
        return render(request, 'lemni/artists_list.html', context)


class ArtistDetail(View):
    def get(self, request, slug):
        # artist = Artist.objects.all() # filter by slug
        artist = get_object_or_404(Artist, slug=slug)
        songs = Song.objects.filter(artist__slug=slug)
        albums = Album.objects.filter(artist__slug=slug)
        context = {'artist': artist, 'songs': songs, 'albums': albums}
        return render (request, 'lemni/artist_detail.html', context)

# <!-- {% if album.name != 'None' %} -->
# <!-- {% endif %} -->

class SongsView(View):
    def get(self, request):
        songs = Song.objects.all()
        context = {'songs': songs}
        return render(request, 'lemni/songs_list.html', context)


class SongDetail(View):
    def get(self, request, slug):
        song= get_object_or_404(Song, slug=slug)
        # artist = Artist.objects.get(pk = 1)
        # artist = Artist.objects.filter(song__slug=slug)
        artist = Artist.objects.get(song__slug=slug)
        # feature = Song.objects.get(slug=slug).feature
        # feature = song.feature.filter(song__slug=slug)
        features = song.feature.all()
        # artist = Artist.objects.get(pk=1)
        # genres = Genre.objects.filter(pk=slug[0])
        genres = Genre.objects.filter(song__slug=slug)
        context = {'song': song, 'artist': artist, 'genres': genres,
                   'features': features
                   }
        print(features)

        return render(request, 'lemni/song_detail.html', context)

 # <!-- <a href='{% url "lemni:artist_detail" slug=feature.get  %}'>{% for feature in features  %} {{ feature }} {% endfor %}</a> -->


class AlbumsView(View):
    def get(self, request):
        albums = Album.objects.all()
        # artists = Artist.objects.filter(album__song=)
        context = {'albums': albums}
        return render(request, 'lemni/albums_list.html', context)


class AlbumDetail(View):
    def get(self, request, slug):
        album = Album.objects.get(slug=slug)
        songs = Song.objects.filter(album_id=slug)
        # features = songs.feature.all()
        artist = Artist.objects.filter(slug='Gunna')
        context = {'album': album, 'songs': songs, 'artist': artist,
                   # 'features': features
                   }
        print(songs)

        # for song in songs:
        #     print(song.feature)
        return render(request, 'lemni/album_detail.html', context)




'''
class ArtistSongsView(View):
    def get(self, request, id, slug):
        # if id:
        #     songs = Song.objects.filter(artist=id)
        # else:
        #     songs = Song.objects.all()
        artist = Artist.objects.filter(id=id)
        # songs = Song.objects.filter(artist_slug=artist_slug)
        # songs = Song.objects.filter(slug__startswith="1")
        # songs = Song.objects.filter(slug__startswith= "Artist.pk")
        # songs = Artist.objects.get(id=4).song_set.all()
        # songs = Song.objects.filter(slug="1-praise-lord")
        # songs = Song.objects.filter(slug= "1" + "-praise-lord")
        songs = Song.objects.filter(artist__slug=slug)
        # songs = Song.objects.filter(slug__startswith='1')
        # songs = Song.objects.filter(slug__startswith='1')
        # songs = Song.objects.all()


        # songs = get_object_or_404(Song) Pay attention to it!!!


        # songs = Song.objects.all()
                # if artist_slug:
        #     artist = get_object_or_404(Artist, slug=artist_slug)
        #     songs = Song.objects.filter(artist=artist.id)
        #     # print('HIIIII')
        context = {'songs': songs}
        return render(request, 'lemni/songs_list.html', context)
'''


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
    success_url = reverse_lazy('lemni:registration_done')


class RegistrationDoneView(TemplateView):
    template_name = 'user/registration_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'user/bad_signature.html')
    user = get_object_or_404(MyUser, username=username)
    if user.is_activated:
        template = 'user/user_is_activated.html'
    else:
        template = 'user/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)
