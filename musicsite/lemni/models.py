from django.db import models


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
    draft = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Clip'
        verbose_name_plural = 'Clips'


class Song(models.Model):
    name = models.CharField(max_length=55)
    artist = models.ManyToManyField('Artist', related_name='artist')
    feature = models.ManyToManyField('Artist', related_name='feature', blank=True)
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


class Artist(models.Model):
    alias = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, db_index=True, unique=True)
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
