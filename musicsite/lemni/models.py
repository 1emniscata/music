from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15, db_index=True, unique=True)
    draft = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Musical Genre'
        verbose_name_plural = 'Musical Genres'


class Clip(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)  # there will be a link from YouTube
    slug = models.SlugField(max_length=230, db_index=True, unique=True, primary_key=True)

    draft = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Clip'
        verbose_name_plural = 'Clips'


class Artist(models.Model):
    alias = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, db_index=True, unique=True, primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    genres = models.ManyToManyField(Genre)
    birthday = models.DateField()
    photo = models.ImageField(upload_to='artists')
    description = models.TextField()
    clips = models.ManyToManyField(Clip, blank=True)
    draft = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
        ordering = ['alias']

    def get_absolute_url(self):
        return reverse('lemni:artist_detail', args=[self.slug])



class Album(models.Model):
    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=60, db_index=True, unique=True, primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='al_covers', blank=True)
    release_date = models.DateField(blank=True)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['name']

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('lemni:album_detail', args=[self.slug])


class Song(models.Model):
    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, primary_key=True)
    artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT, default=1)
    feature = models.ManyToManyField(Artist, related_name='feature', blank=True)
    audio_file = models.FileField(default='')
    cover = models.ImageField(upload_to='covers')
    release_date = models.DateField()
    description = models.TextField()
    lyrics = models.CharField(max_length=100)  # there will be a link to Genius
    genre = models.ManyToManyField(Genre)
    draft = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('lemni:song_detail', args=[self.slug])


class MyUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Passed activation')
    send_messages = models.BooleanField(default=True, verbose_name='Receiving of email notifications')

    class Meta(AbstractUser.Meta):
        pass
