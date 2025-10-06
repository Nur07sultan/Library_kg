from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import random
from . import models 

# === ListView ===
def book_list_view(request):
    if request.method == 'GET':
        books = models.Books.objects.all()
        context = {
            'books': books, 
        }
        return render(request, template_name='books/books_list.html', context=context)
    
# === DetailView с поддержкой отзывов ===
def book_detail_view(request, id):
    book = get_object_or_404(models.Books, id=id)
    reviews = book.reviews.all()  # получаем все отзывы книги

    # Обработка отправки нового отзыва
    if request.method == "POST":
        rating = int(request.POST.get('rating', 1))
        text = request.POST.get('text', '')
        if text:
            models.Review.objects.create(book=book, rating=rating, text=text)

    context = {
        'book_id': book,
        'reviews': reviews,
    }
    return render(request, template_name='books/book_detail.html', context=context)

# === Прочие функции остаются без изменений ===
def current_time(request):
    now = timezone.localtime(timezone.now())
    return HttpResponse(f"Текущее время: {now.strftime('%H:%M:%S')}")

def random_number(request):
    number = random.randint(1, 100)
    return HttpResponse(f"Случайное число: {number}")

def about_me(request):
    if request.method == 'GET':
        return HttpResponse(
            "Меня зовут Нурсултан, мне 17 лет. Я учусь в GEEKS 4 месяц на Backend разработке.\n"
            "Так же занимаюсь боксом "
        )






