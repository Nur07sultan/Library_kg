from django.contrib import admin
from .models import Channel, CineItem
from .models import Genre, Tag, Rating, Movie
from .models import MovieComment
from django.contrib import admin

# Adjust the global admin site headers to mention CineBoard context
admin.site.site_header = 'Library.kg — Администрирование'
admin.site.site_title = 'Library.kg Admin'
admin.site.index_title = 'Управление сайтом'

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(CineItem)
class CineItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel', 'created_at')
    search_fields = ('title', 'channel__name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating', 'created_by', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('release_date', 'rating')
    filter_horizontal = ('genres', 'tags')
    
    def title_display(self, obj):
        return obj.title
    title_display.short_description = 'Название'


@admin.register(MovieComment)
class MovieCommentAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at')
    search_fields = ('movie__title', 'user__username', 'text')
