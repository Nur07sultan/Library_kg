from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    description = models.TextField(verbose_name='Напишите описание книги')
    image = models.ImageField(upload_to='books/', verbose_name='Выберите изображение книги')
    quantity_page = models.PositiveIntegerField(verbose_name='Количество страниц')
    author = models.CharField(max_length=100, blank=True, verbose_name='Автор книги')
    book_audio = models.URLField(blank=True, null=True, verbose_name='Ссылка на аудиокнигу')
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
