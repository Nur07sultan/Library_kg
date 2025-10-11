from django.contrib import admin
from .models import Books, Review, Tour, Registration, Episode

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1
    fields = ('order', 'title', 'video_url', 'video_file')
    ordering = ('order',)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity_page', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)
    inlines = [EpisodeInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'text')
    list_filter = ('rating',)
    search_fields = ('book__title', 'text')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'tour')
    search_fields = ('full_name', 'tour__name')

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('book', 'order', 'title', 'video_url', 'video_file')
    list_filter = ('book',)
    search_fields = ('book__title', 'title')
    ordering = ('book', 'order')








