from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import ArtistsView, ArtistDetail, main, SongsView, ClipsView, LemniLoginView, SongDetail, \
    profile, RegistrationUserView, RegistrationDoneView, user_activate, AlbumsView, AlbumDetail

# from .views import ArtistSongsView

app_name = 'lemni'

urlpatterns = [
    path('', main, name='main'),
    path('accounts/login/', LemniLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='lemni:main'), name='logout'),
    path('accounts/register/', RegistrationUserView.as_view(), name='registration'),
    path('accounts/register/activate/<str:sign>', user_activate, name='registration_activate'),
    path('accounts/register/done', RegistrationDoneView.as_view(), name='registration_done'),
    path('accounts/profile/', profile, name='profile'),
    path('artists/', ArtistsView.as_view(), name='artists_list'),
    # path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$' , ArtistDetail.as_view(), name='artist_detail'),
    path('artists/<slug:slug>/', ArtistDetail.as_view(), name='artist_detail'),
    path('songs/', SongsView.as_view(), name='songs_list'),
    path('songs/<slug:slug>/', SongDetail.as_view(), name='song_detail'),
    path('albums/', AlbumsView.as_view(), name='albums_list'),
    path('albums/<slug:slug>/', AlbumDetail.as_view(), name='album_detail'),
    # path('songs/<id>/<slug:slug>/', ArtistSongsView.as_view(), name='artist_songs_list'),
    # path('songs/<id>/<slug:slug>/', ArtistSongsView.as_view(), name='artist_songs_list'),
    path('clips/', ClipsView.as_view(), name='clips_list'),
]
