from django.contrib import admin
from . import models

# === Книги ===
@admin.register(models.Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity_page', 'created_at')

# === Отзывы ===
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'text')

# === Туры ===
@admin.register(models.Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name',)

# === Регистрации ===
@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'tour')  # здесь вместо user теперь full_name
    search_fields = ('full_name',)       # можно искать по имени участника
    list_filter = ('tour',)              # фильтр по туру



