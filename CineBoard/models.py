from django.db import models

# Minimal models for CineBoard — extend later
class Channel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Канал')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'

class CineItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('cineboard:item_detail', args=[self.id])
    class Meta:
        verbose_name = 'Элемент Cine'
        verbose_name_plural = 'Элементы Cine'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('cineboard:movie_detail', args=[self.id])


# === Movie-related models ===
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Жанр')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Тег')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Rating(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Рейтинг (админ)')
    value = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name='Значение (опционально)')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Movie(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    genres = models.ManyToManyField(Genre, blank=True, related_name='movies', verbose_name='Жанры')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода')
    rating = models.ForeignKey(Rating, null=True, blank=True, on_delete=models.SET_NULL, related_name='movies', verbose_name='Рейтинг (админ)')
    tags = models.ManyToManyField(Tag, blank=True, related_name='movies', verbose_name='Теги (админ)')
    poster = models.ImageField(upload_to='movies/posters/', null=True, blank=True, verbose_name='Постер')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='movies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('cineboard:movie_detail', args=[self.id])

    class Meta:
        ordering = ['-created_at']



# Комментарии к фильмам
class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_comments')
    rating = models.IntegerField(null=True, blank=True, verbose_name='Оценка (1-5)')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий к фильму'
        verbose_name_plural = 'Комментарии к фильмам'

    def __str__(self):
        return f"{self.user} on {self.movie.title}: {self.text[:40]}"
