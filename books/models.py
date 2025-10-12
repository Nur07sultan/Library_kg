from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# === Модель книги ===
class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    description = models.TextField(verbose_name='Описание книги')
    image = models.ImageField(upload_to='books/', verbose_name='Изображение книги')
    quantity_page = models.PositiveIntegerField(verbose_name='Количество страниц')
    author = models.CharField(max_length=100, blank=True, verbose_name='Автор книги')
    book_audio = models.URLField(blank=True, null=True, verbose_name='Ссылка на аудиокнигу')
    book_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на книгу')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum([r.rating for r in reviews]) / reviews.count()
        return 0

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


# === Модель отзывов ===
class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews', verbose_name='Книга')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Рейтинг')
    text = models.TextField(verbose_name='Отзыв')

    def __str__(self):
        return f"{self.book.title} - {self.rating}"

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


# === Модель туров ===
class Tour(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тура')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'туры'


# === Модель регистрации на тур ===
class Registration(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='ФИО участника')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')

    def __str__(self):
        return f"{self.full_name} - {self.tour.name}"

    class Meta:
        verbose_name = 'регистрация'
        verbose_name_plural = 'регистрации'
        constraints = [
            models.UniqueConstraint(fields=['full_name'], name='unique_participant')
        ]


# === Модель серий видео ===
class Episode(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='episodes', verbose_name='Книга')
    title = models.CharField(max_length=100, verbose_name='Название серии')
    order = models.PositiveIntegerField(default=1, verbose_name='Порядок серии')
    video_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео (YouTube, Rutube и т.д.)')
    video_file = models.FileField(upload_to='episodes/', blank=True, null=True, verbose_name='Локальный файл видео')

    def __str__(self):
        return f"{self.book.title} - Серия {self.order}: {self.title}"

    def embed_url(self):
        """Возвращает ссылку, подходящую для iframe"""
        if self.video_url:
            if "youtube.com/watch?v=" in self.video_url:
                return self.video_url.replace("watch?v=", "embed/")
            elif "rutube.ru/video/" in self.video_url:
                return self.video_url.replace("rutube.ru/video/", "rutube.ru/play/embed/").split("?")[0]
        return self.video_url

    class Meta:
        verbose_name = 'серия'
        verbose_name_plural = 'серии'
        ordering = ['order']







 








