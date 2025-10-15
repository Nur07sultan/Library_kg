from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import random
from . import models

# === ListView ===
def book_list_view(request):
    books = models.Books.objects.all()
    return render(request, 'books/books_list.html', {'books': books})

# === DetailView с сериями и отзывами ===
def book_detail_view(request, id, episode_id=None):
    book = get_object_or_404(models.Books, id=id)
    reviews = book.reviews.all()
    episodes = book.episodes.all()
    
    if episode_id:
        current_episode = get_object_or_404(models.Episode, id=episode_id, book=book)
    else:
        current_episode = episodes.first() if episodes.exists() else None

    # Добавление отзыва
    if request.method == "POST" and 'text' in request.POST:
        rating = int(request.POST.get('rating', 1))
        text = request.POST.get('text', '')
        if text:
            models.Review.objects.create(book=book, rating=rating, text=text)

    context = {
        'book': book,
        'reviews': reviews,
        'episodes': episodes,
        'current_episode': current_episode,
    }
    return render(request, 'books/book_detail.html', context)

# === Дополнительные функции ===
def current_time(request):
    now = timezone.localtime(timezone.now())
    return HttpResponse(f"Текущее время: {now.strftime('%H:%M:%S')}")

def random_number(request):
    number = random.randint(1, 100)
    return HttpResponse(f"Случайное число: {number}")

def about_me(request):
    return HttpResponse(
        "Меня зовут Нурсултан, мне 17 лет. Я учусь в GEEKS 4 месяц на Backend разработке.\n"
        "Так же занимаюсь боксом "
    )
