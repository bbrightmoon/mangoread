from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    name = models.CharField(max_length=100, verbose_name='название жанра')

    def __str__(self):
       return self.name

class Card(models.Model):
    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'
    image = models.URLField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='дата изменения')
    title = models.CharField(max_length=250, unique=True, verbose_name='название')
    description = models.TextField(blank=True, verbose_name="Синопсис")
    year = models.IntegerField(verbose_name="Год", null=True)
    genre = models.ManyToManyField(Genre, related_name='genres')


    def __str__(self):
        return self.title

    def get_genre_list_from_m(self):
        return [i.name for i in self.genre.all()]



class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')
    text = models.TextField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return self.text




























