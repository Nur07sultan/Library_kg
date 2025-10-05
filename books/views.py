from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import random
from . import models 

#Listview
def book_list_view(request):
    if request.method == 'GET':
        books = models.Books.objects.all()
        context = {
            'books': books, 
        }
        return render(request, template_name='books/books_list.html', context=context)
    
#Detailview
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {
            'book_id': book_id,
        }
        return render(request, template_name='books/book_detail.html', context=context)

def current_time(request):
    now = timezone.localtime(timezone.now())
    return HttpResponse(f"Текущее время: {now.strftime('%H:%M:%S')}")

def random_number(request):
    number = random.randint(1, 100)
    return HttpResponse(f"Случайное число: {number}")

def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Меня зовут Нурсултан, мне 17 лет. Я учусь в GEEKS 4 месяц на Bakend разработке.\n"
"Так же занимаюсь боксом ")




