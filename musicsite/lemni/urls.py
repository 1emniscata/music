from django.urls import path
from . import views
from .views import ArtistsView, ArtistDetail,  main, SongsView, ClipsView

app_name = 'lemni'

urlpatterns = [
    path('', main, name='main'),
    path('artists/', ArtistsView.as_view(), name='artists_list'),
    path('artists/artist', ArtistDetail.as_view(), name='artist_detail'),
    path('songs/', SongsView.as_view(), name='songs_list'),
    path('clips/', ClipsView.as_view(), name='clips_list'),
]
